# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import TencentPosition


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php']

    def parse(self, response):
        tr_list = response.xpath('//table[@class="tablelist"]//tr[@class="even" or @class="odd"]')
        for tr in tr_list:
            item = TencentPosition()
            item["position_name"] = tr.xpath('./td/a/text()').extract_first()
            item["position_type"] = tr.xpath('./td[2]/text()').extract_first()
            item["num"] = tr.xpath('./td[3]/text()').extract_first()
            item["address"] = tr.xpath('./td[4]/text()').extract_first()
            item["publish_time"] = tr.xpath('./td[5]/text()').extract_first()
            yield item

        # 获取下一页连接
        next_page_url = response.xpath('//table[@class="tablelist"]//tr//a[@id="next"]/@href').extract_first()
        if next_page_url != 'javascript:;':
            next_page_url = 'https://hr.tencent.com/' + next_page_url
            yield scrapy.Request(
                next_page_url,
                callback=self.parse
            )







