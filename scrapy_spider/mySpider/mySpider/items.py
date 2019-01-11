# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    img_url = scrapy.Field()
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()


class TencentPosition(scrapy.Item):
    """
    腾讯职位Item
    """
    position_name = scrapy.Field()
    position_type = scrapy.Field()
    num = scrapy.Field()
    address = scrapy.Field()
    publish_time = scrapy.Field()


class SunHotlineItem(scrapy.Field):
    """
    阳光热线问政平台Item
    """
    info_id = scrapy.Field()  # 编号
    title = scrapy.Field()  # 标题
    relate_department_name = scrapy.Field()  # 关联部门
    relate_department_url = scrapy.Field()  # 关联部门地址
    status = scrapy.Field()  # 状态
    net_friend_name = scrapy.Field()  # 网友名
    publish_time = scrapy.Field()  # 发布日期
    info_detail = scrapy.Field()  # 详细信息
    image_url = scrapy.Field()  # 图片地址



