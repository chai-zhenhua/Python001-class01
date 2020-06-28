# -*- coding: utf-8 -*-
import scrapy


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):


    def parse(self, response):
        pass
