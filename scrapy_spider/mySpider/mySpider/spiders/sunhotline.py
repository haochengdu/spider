# -*- coding: utf-8 -*-
import scrapy

from mySpider.items import SunHotlineItem


class SunhotlineSpider(scrapy.Spider):
    name = 'sunhotline'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0', ]

    def parse(self, response):
        tr_list = response.xpath('//td[@align="center"]//tr')
        for tr in tr_list:
            item = SunHotlineItem()
            item['info_id'] = tr.xpath('./td[1]/text()').extract_first()
            item['title'] = tr.xpath('./td[2]/a[2]/text()').extract_first()
            item['relate_department_name'] = tr.xpath('./td[2]/a[3]/text()').extract_first()
            relate_department_url = tr.xpath('./td[2]/a[3]/@href').extract_first()
            item['relate_department_url'] = 'http://wz.sun0769.com' + relate_department_url
            item['status'] = tr.xpath('./td[3]/span/text()').extract_first()
            item['net_friend_name'] = tr.xpath('./td[4]/text()').extract_first()
            item['publish_time'] = tr.xpath('./td[5]/text()').extract_first()

            item_detail_url = tr.xpath('./td[2]/a[2]/@href').extract_first()  # 详情页交给下一个解析方法
            yield scrapy.Request(
                item_detail_url,
                callback=self.detail_parse,
                meta={'item': item},
            )

        # 获取下一页连接方式1(获取不全)
        # if response.xpath('//div[@class="pagination"]/a[last()-1]/text()').extract_first() == '>':
        #     next_page_url = response.xpath('//div[@class="pagination"]/a[last()-1]/@href').extract_first()
        #     yield scrapy.Request(
        #         next_page_url,
        #         callback=self.parse,
        #     )
        # 获取下一页连接方式2，根据页数获取
        next_page_url = response.xpath('//div[@class="pagination"]/a[last()-1]/@href').extract_first()
        cur_page = response.xpath('//span[@class="cur"]/text()').extract_first().strip()
        cur_page = int(cur_page)
        if isinstance(cur_page, int):
            if cur_page < 3424:
                next_page_url = 'http://wz.sun0769.com/index.php/question/questionType?type=4&page=' + str(cur_page * 30)
        yield scrapy.Request(
            next_page_url,
            callback=self.parse,
        )

    def detail_parse(self, response):
        """
        详情页解析
        :return:
        """
        """
        带图片
        //div[@class="wzy1"]//td[@class="txt16_3"][1]/div[@class="textpic"]/img/@src
        //div[@class="wzy1"]//td[@class="txt16_3"][1]/div[@class="contentext"]/text()
        不带图片
        //div[@class="wzy1"]//td[@class="txt16_3"][1]/text()
        """
        item = response.meta['item']
        td_selectors = response.xpath('//div[@class="wzy1"]//td[@class="txt16_3"][1]')
        # 带图片
        div_img_list = td_selectors.xpath('./div[@class="textpic"]/img/@src').extract()
        if div_img_list:
            info_detail_list = td_selectors.xpath('./div[@class="contentext"]/text()').extract()
            info_detail_list = [info.strip() for info in info_detail_list]
            item['info_detail'] = ''.join(info_detail_list)
            div_img_list = ['http://wz.sun0769.com' + img for img in div_img_list]
            item['image_url'] = div_img_list
        else:
            info_detail_list = response.xpath('//div[@class="wzy1"]//td[@class="txt16_3"][1]/text()').extract()
            info_detail_list = [info.strip() for info in info_detail_list]
            item['info_detail'] = ''.join(info_detail_list)
            item['image_url'] = None
        yield item



