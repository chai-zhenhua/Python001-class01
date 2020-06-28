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
        cookie = '__mta=146044427.1593337411652.1593337411652.1593337411652.1;' ' uuid_n_v=v1; ' 'uuid=D2A2CCE0B92311EAA94453F28D7995DF136E9C239CE54B49884F5EDB075757A3; ' '_csrf=7191ff74d070b7024355dbc27a7aa6e4c93b975adf782870304f6f92dccba15c; ' 'Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592986956,1593076672,1593096084,1593337394; ' '_lxsdk_cuid=172e56bef4dc8-08ad4c59b813bd-31607403-fa000-172e56bef4dc8; ' '_lxsdk=D2A2CCE0B92311EAA94453F28D7995DF136E9C239CE54B49884F5EDB075757A3; ' 'mojo-uuid=49838d8e729158513762de8e12e2af53; ' 'Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593337411;' ' _lxsdk_s=172fa4f5efd-99b-ea-43c%7C308984839%7C2'
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url=url,cookies=cookie,callback=self.parse)

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