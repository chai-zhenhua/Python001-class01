'''
作业1：
    安装并使用requests、bs4库，爬取猫眼电影的前10个电影名称、电影类型和上映时间，并以UTF-8字符集保存到csv格式的文件中。

    解题思路：
        使用html和lxml两种方式来完成，巩固所学知识。
        1、先使用requests获取网页源代码
        2、使用bs4解析，匹配电影名称和链接
        3、再次请求电影链接进入详情页获取电影类型和上映时间
        4、前10个我选择使用字典记录爬取到的信息，每条记录是一个k/v，计算字典长度来控制爬取个数
'''

import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from lxml import etree
import pandas

#请求头伪造
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1'
Cookie = {
    "__mta" : "207976749.1593239934090.1593239934090.1593239934090.1",
    "uuid_n_v" : "v1",
    "uuid" : "DBEF6B20B84011EAB787AF911C0DA1B79D43D5D2785F4E048B9D77842C2BE1F7",
    "_csrf" : "bea4b91d22739c223995862945de3dd6bf9902390b38ad2c1bda3b3770e5aec2",
    "Hm_lvt_703e94591e87be68cc8da0da7cbd0be2" : "1592986956,1593076672,1593096084",
    "_lxsdk_cuid" : "172e56bef4dc8-08ad4c59b813bd-31607403-fa000-172e56bef4dc8",
    "_lxsdk" : "DBEF6B20B84011EAB787AF911C0DA1B79D43D5D2785F4E048B9D77842C2BE1F7",
    "mojo-uuid" : "49838d8e729158513762de8e12e2af53",
    "Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2" : "1593239930",
    "_lxsdk_s" : "172f47fc60c-16c-2e1-026%7C308984839%7C2"
}
headers = {'user-agent':user_agent}

#定义字典，把爬取的结果存放在字典中
item = {}

def get_detail(url):
    '''获取电影详情'''
    r = requests.get(url,headers=headers,cookies=Cookie)
    result = etree.HTML(r.text)

    #电影类型
    film_type = result.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[1]/a/text()'.strip())

    #上映时间
    film_time = result.xpath('/html/body/div[3]/div/div[2]/div[1]/ul/li[3]/text()'.strip())
    return film_type,film_time

def get_info(url,num=10):
    '''获取电影名称和链接'''

    #初始化列表
    data = []
    r = requests.get(url=url,headers=headers)
    bs_info = bs(r.text,'html.parser')

    for tag in bs_info.find_all('div',attrs={'class':'channel-detail movie-item-title'}):
        #获取电影名称
        title = tag.get('title')

        #获取链接
        for atag in tag.find_all('a'):
            link = 'https://maoyan.com' + atag.get('href')
            sleep(10)

        item[title] = link

        #调用函数，获取电影类型和上映时间
        type,time = get_detail(url=link)

        #最终的影片信息存储到列表中，便于后续保存为csv
        data.append([title,type,time])

        # 只取前num个电影
        if len(item) == num:
            # 保存为csv格式
            movie = pandas.DataFrame(data=data)
            movie.to_csv('./movies.csv', encoding='utf8',index=False, header=False, )
            break

url = 'https://maoyan.com/films?showType=3'

if __name__ == '__main__':
    get_info(url=url)