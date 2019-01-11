# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from mySpider.utils.mongodb_util import MongoBD
from mySpider.items import TencentPosition, SunHotlineItem

logger = logging.getLogger(__name__)


class MyspiderPipeline(object):

    def process_item(self, item, spider):

        return item


class TencentPositionPipeline(object):

    def __init__(self):
        host_ip = '192.168.2.223'
        port = 27017
        db_name = 'spider'
        collection_name = 'tencentposition'
        self.mongodb = MongoBD(host_ip, port)
        self.collection = self.mongodb.get_collection(db_name, collection_name)

    def process_item(self, item, spider):
        if isinstance(item, TencentPosition):
            self.collection.insert_one(dict(item))
            logger.info('存入MongoDB= {}'.format(dict(item)))
        return item

    def close_spider(self, spider):
        self.mongodb.close()
        logger.info('爬完毕')


class SunHotlinePipeline(object):
    """
    阳光热线问政平台pipeline
    """

    def __init__(self):
        host_ip = '192.168.2.223'
        port = 27017
        db_name = 'spider'
        collection_name = 'sunhotline2'
        self.mongodb = MongoBD(host_ip, port)
        self.collection = self.mongodb.get_collection(db_name, collection_name)

    def process_item(self, item, spider):
        if isinstance(item, SunHotlineItem):
            self.collection.insert_one(dict(item))
            # logger.info('存入MongoDB= {}'.format(dict(item)))
        return item

    def close_spider(self, spider):
        self.mongodb.close()
        logger.info('sunhotline2爬完毕')












