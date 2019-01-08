# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'  # 这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字。
    allowed_domains = ['itcast.cn']  # 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略。
    # 爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成。
    start_urls = ("http://www.itcast.cn/channel/teacher.shtml",)

    def parse(self, response):
        """
        解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下：
        负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
        生成需要下一页的URL请求。
        :param response:
        :return:
        """
        pass
