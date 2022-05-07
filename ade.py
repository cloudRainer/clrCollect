import asyncio
from shttp import asyn
from bs4 import BeautifulSoup
from sdb import stores
import requests


def callbask(task):
    res = task.result()
    if res['status'] == 200:
        soup = BeautifulSoup(res['text'], "lxml")

        data = {
            'title':res['title'],
            'url':res['url'],
            'content':soup.select_one('.content').text,
        }
        stores.ClrBookItem.insert(data).execute()
        print(res['url'],"Done")
url = "http://book.zongheng.com/showchapter/1213435.html"
main_res = requests.get(url)
if main_res.status_code == 200:
    soup = BeautifulSoup(main_res.text, "lxml")
    urls = [(x.get("href"),{'title':x.text,'url':x.get("href")}) for x in soup.select(".col-4 > a")]
    asyncio.run(asyn.fetch(urls,callbask))


