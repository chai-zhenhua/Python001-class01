# -*- coding: utf-8 -*-
import pandas as pd

'''生成csv文件需要在settings中打开pipelines的配置'''

class Zuoye2Pipeline:
    def process_item(self, item, spider):
        title = item['title']
        type = item['type']
        time = item['time']

        output = [f'{title}  {type}  {time}']
        movie = pd.DataFrame(data=output)
        movie.to_csv('../movies2.csv',mode='a',encoding='utf8',index=False,header=False)
        return item
