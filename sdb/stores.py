# -*- coding: utf-8 -*-
# @Author : ShuBo
# @File : stores.py
# @Project: diy
# @CreateTime : 2022/5/6 22:01
# @Info :
from peewee import *

import setting
database = MySQLDatabase(setting.store_db['db'],
                         **{'charset': 'utf8', 'sql_mode': 'PIPES_AS_CONCAT', 'use_unicode': True,
                            'host': setting.store_db['host'], 'port': setting.store_db['port'],
                            'user': setting.store_db['user'], 'password': setting.store_db['password'],
                            'connect_timeout': 60 * 60 * 48})
class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class ClrBookItem(BaseModel):
    content = TextField(null=True)
    title = CharField(null=True)
    url = CharField(null=True)

    class Meta:
        table_name = 'clr_book_item'
