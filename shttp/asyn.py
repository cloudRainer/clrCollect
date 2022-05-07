# -*- coding: utf-8 -*-
# @Author : ShuBo
# @File : asyn.py
# @Project: hs_collection
# @CreateTime : 2022/5/1 22:50
# @Info :
import asyncio
import traceback
import aiohttp
import random
from .cache import agent_pools

# 设置超时
timeout = aiohttp.ClientTimeout(total=15)


def getHeader():
    '''
    header配置，User-Agent随机取出
    :return:
    '''
    header = {
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
        "Cache-Control":"max-age=0",
        "Connection":"keep-alive",
        "sec-ch-ua-mobile":"?0",
        "Sec-Fetch-Dest":"document",
        "Sec-Fetch-Mode":"navigate",
        "Sec-Fetch-Site":"same-site",
        "Sec-Fetch-User":"?1",
        "Upgrade-Insecure-Requests":"1",
        "User-Agent":random.choice(agent_pools)
    }
    return header

async def fetch(data,callback,sem_number=3,proxy=False):
    '''
    采集主程序
    :param data:[(采集地址,传参)]
    :param callback: 回调函数
    :param sem_number: 并发数量
    :param proxy: 是否开启代理【预留】
    :return:
    '''
    sem = asyncio.Semaphore(sem_number)
    tasks = []
    for x in data:
        task = asyncio.create_task(fetch_item(x[0],x[1],sem))
        task.add_done_callback(callback)
        tasks.append(task)
    await asyncio.wait(tasks)

async def fetch_item(url, res,sem,ip=''):
    '''
    采集明细
    :param url:地址
    :param res: 传参
    :param sem: 并发
    :param ip: 代理IP预留
    :return:
    '''
    try:
        async with sem:
            async with aiohttp.ClientSession(timeout=timeout) as s:
                async with s.get(url, headers=getHeader(), proxy=ip, verify_ssl=False) as response:
                    res['status'] = response.status
                    if res['status'] == 200:
                        res['text'] = await response.text()
                    return res
    # 超时
    except asyncio.TimeoutError as timeout_error:
        res['status'] = 0
        return res
    # 未知异常
    except Exception:
        res['status'] = 0
        res['error'] = traceback.format_exc()
        return res

async def get(url):
    '''
    单条采集
    :param url:
    :return:
    '''
    async with aiohttp.ClientSession(timeout=timeout) as s:
        async with s.get(url, headers=getHeader(),verify_ssl=False) as response:
            res = {}
            res['status'] = response.status
            if res['status'] == 200:
                res['text'] = await response.text()
            return res