# -*- coding: utf-8 -*-

import pymysql

class MysqlItemPipline(object):
    def __init__(self, host, database, table, user, password, port):
        self.host = host
        self.database = database
        self.table = table
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('HOST'),
            database=crawler.settings.get('DATABASE'),
            table=crawler.settings.get('TABLE'),
            user=crawler.settings.get('USER'),
            password=crawler.settings.get('PASSWORD'),
            port=crawler.settings.get('PORT'),
        )

    def process_item(self, item, spider):

        conn = pymysql.Connect(
        host=self.host,
        user=self.user,
        password=self.password,
        database=self.database,
        charset='utf8mb4',
        port=self.port
        )

        sql = ('insert into %s (title,type,time) values ("%s","%s","%s")'%(self.table,item['title'],item['type'],item['time']))
        print(sql)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
            print('数据插入完成')
        except Exception as e :
            conn.rollback()
            print('数据插入失败，已回滚',e)
        finally:
            conn.close()
        return item
