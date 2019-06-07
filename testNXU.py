# -*- coding: utf-8 -*-
import scrapy


class TestnxuSpider(scrapy.Spider):
    name = 'testNXU'
    allowed_domains = ['www.nxu.edu.cn']
    start_urls = ['http://www.nxu.edu.cn/']

    def parse(self, response):
        pass
