#!/usr/bin/python3.5.2
# -*- coding: utf-8 -*-
"""
@Time    : 2019/1/11 11:16
@Author  : TX
@File    : mongodb_util.py
@Software: PyCharm
"""
import pymongo


class MongoBD(object):
    __instance = None
    __first_init = False

    def __new__(cls, host_ip, port):
        if not cls.__instance:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, host_ip, port):
        """
        :param host_ip: MongoDB IP
        :param port: MongoDB port
        """
        if not self.__first_init:
            self.host_ip = host_ip
            self.port = port
            self.mongo_client = pymongo.MongoClient(host=self.host_ip, port=self.port)
            self.__first_init = True

    def get_collection(self, db_name, collection_name):
        """
        获取集合
        :param db_name: 数据库名
        :param collection_name: 集合名
        :return: 返回集合
        """
        db = self.mongo_client[db_name]  # 指定数据库
        collection = db[collection_name]  # 指定集合
        return collection

    def close(self):
        self.mongo_client.close()


