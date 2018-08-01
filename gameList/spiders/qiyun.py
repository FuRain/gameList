# -*- coding: utf-8 -*-
import scrapy


class QiyunSpider(scrapy.Spider):
    name = 'qiyun'
    allowed_domains = ['qiyun.org']
    start_urls = ['http://www.gamersky.com/news/pc/zx/']

    def parse(self, response):
        print response.body
        pass
