# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from zuoye2.items import Zuoye2Item
from time import sleep


class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    def start_requests(self):
        Cookie = {
            "__mta": "207976749.1593239934090.1593239934090.1593239934090.1",
            "uuid_n_v": "v1",
            "uuid": "DBEF6B20B84011EAB787AF911C0DA1B79D43D5D2785F4E048B9D77842C2BE1F7",
            "_csrf": "bea4b91d22739c223995862945de3dd6bf9902390b38ad2c1bda3b3770e5aec2",
            "Hm_lvt_703e94591e87be68cc8da0da7cbd0be2": "1592986956,1593076672,1593096084",
            "_lxsdk_cuid": "172e56bef4dc8-08ad4c59b813bd-31607403-fa000-172e56bef4dc8",
            "_lxsdk": "DBEF6B20B84011EAB787AF911C0DA1B79D43D5D2785F4E048B9D77842C2BE1F7",
            "mojo-uuid": "49838d8e729158513762de8e12e2af53",
            "Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2": "1593239930",
            "_lxsdk_s": "172f47fc60c-16c-2e1-026%7C308984839%7C2"
        }
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url,cookies=Cookie,callback=self.parse)

    def parse(self, response):
     #   print(response.text)
        item = Zuoye2Item()
        movies = Selector(response=response).xpath('//div[@class="movie-item-hover"]')

        #使用列表分片获取前10个电影
        for movie in movies[:10]:
            title = movie.xpath('./a/div/div[1]/span/text()').extract_first().strip()
            type = movie.xpath('./a/div/div[2]/text()[2]').extract_first().strip()
            time = movie.xpath('./a/div/div[4]/text()[2]').extract_first().strip()
            sleep(30)
            #返回数据给items.py
            item['title'] = title
            item['type'] = type
            item['time'] = time
            yield item