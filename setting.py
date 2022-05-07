# -*- coding: utf-8 -*-
# @Author : ShuBo
# @File : setting.py
# @Project: diy
# @CreateTime : 2022/4/21 14:12
# @Info :配置文件
import logging
import os
redis = {
    'host': "*",
    'decode_responses': True,
    'port': 0,
    'password': '*',
}


store_db = {
    'host': '127.0.0.1',
    'port': 3306,
    'user': 'root',
    'password': 'root',
    'db': 'clr_collection'
}

base_path = os.path.realpath("./")
log_level = logging.DEBUG
