# -*- coding: utf-8 -*-
import scrapy
from spider_week02.items import SpiderWeek02Item
from scrapy.selector import Selector
from time import sleep


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
#    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'

        cookies = {
            "__mta": "121552311.1593939374889.1593939374889.1593939374889.1",
            "uuid_n_v": "v1",
            "uuid": "60A28CF0BE9D11EAA582DFDB8874C66988A49522306448EDA5CE88BE9C18D08F",
            "_csrf": "a8ddd61841cf9a0b8955b9e64064e5f8adbf50e532b442f5b09077a9995332e5",
            "Hm_lvt_703e94591e87be68cc8da0da7cbd0be2": "1593337394,1593411552,1593939355,1593939374",
            "_lxsdk_cuid": "172e56bef4dc8-08ad4c59b813bd-31607403-fa000-172e56bef4dc8",
            "_lxsdk": "60A28CF0BE9D11EAA582DFDB8874C66988A49522306448EDA5CE88BE9C18D08F",
            "mojo-uuid": "49838d8e729158513762de8e12e2af53",
            "Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2": "1593939374",
            "_lxsdk_s": "1731e30ab22-ef2-d39-60e%7C308984839%7C2"
        }
        yield scrapy.Request(url=url,cookies=cookies,callback=self.parse)

    def parse(self, response):
        item = SpiderWeek02Item()
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]')
        # 使用列表分片获取前10个电影
        for movie in movies[:10]:
            title = movie.xpath('./a/div/div[1]/span/text()').extract_first().strip()
            type = movie.xpath('./a/div/div[2]/text()[2]').extract_first().strip()
            time = movie.xpath('./a/div/div[4]/text()[2]').extract_first().strip()
            sleep(30)
            item['title'] = title
            item['type'] = type
            item['time'] = time
            yield item