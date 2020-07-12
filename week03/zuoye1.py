import argparse
from ping3 import ping
from threading import Thread
from queue import Queue
import re
import itertools


class GetData(object):
    def __init__(self, ip_ranage):
        self.ip_queue = Queue()
        if '-' in ip_ranage:
            # 把ip地址段转化为ip列表
            first_ip = re.search('[0-9]+.[0-9]+.[0-9]+.[0-9]+', ip_ranage)  # 获取IP地址段的第一个ip
            ip_prefix = re.search('[0-9]+.[0-9]+.[0-9]+', first_ip.group())  # 获取IP地址段的前缀（这里计算不太严谨，没有考虑子网掩码）
            start_point = re.search('[0-9]+$', first_ip.group())  # 获取IP地址的开始数字；比如10.10.10.21,这里获取21
            end_point = re.search('[0-9]+$', ip_ranage)  # 获取结尾

            # print(type(int(start_point.group())))

            ip_list = []
            for n in range(int(start_point.group()), int(end_point.group())):
                ip = f'{ip_prefix.group()}.{n}'
                ip_list.append(ip)
            self.ip_list = ip_list
        else:
            self.ip_list = ip_ranage

        ports = list(range(1, 1025))  # ports
        # 组合IP & ports
        ip_pools = itertools.product(ip_list, ports)
        for ip_pool in ip_pools:
            self.ip_queue.put(ip_pool)

        # -w 输出
        output_address = ''


class Check(Thread):
    '''检测网络联通和端口开放'''

    def __init__(self, ipQueue):  # q: 存放ip 和 port 的数据队列
        super().__init__()
        self.ipQueue = ipQueue

    def run(self):
        '''重写run方法'''
        print(f'线程{Thread.getName()}启动')
        self.check_ping()
        print(f'线程{Thread.getName()}结束')

    def check_ping(self):
        while True:
            if self.ipQueue.empty():
                break
            else:
                try:
                    ipaddr, port = self.ipQueue.get()
                except Exception as f:
                    print(f'发生异常： {f}')

    def Ping(self):
        pass

    def check_port(self):
        pass


if __name__ == '__main__':
# #defina command line args
# parse = argparse.ArgumentParser(description='接收命令行参数')
# parse.add_argument('-n',dest='Number',required=True,default=0,help='指定并发数量',type=int) #接收并发数
# parse.add_argument('-f',dest='Protocol',required=True,default='',help='指定使用tcp or ping',type=str) #接收操作类型
# parse.add_argument('-ip',dest='Ip',required=True,default='',help='指定IP or IP ranage',type=str) #接收ip范围
# parse.add_argument('-w',dest='File',required=False,default='',help='指定保存文件',type=str) #接收保存文件名和位置
#
# args = parse.parse_args()
#
# #分配参数
# command_n = args.Number
# command_f = args.Protocol
# command_ip = args.Ip
# command_w = args.File
    pass





