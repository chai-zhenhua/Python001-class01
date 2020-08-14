"""
作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。
"""

import time


def timer(func):
    """定义一个timer装饰器，实现记录程序的执行花费时间"""
    def inner(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        use_time = end_time - start_time
        print(f'程序执行花费时间是{use_time}')
        return result  # 返回程序的返回值

    return inner


@timer  # f1 = timer(f1)
def f1(a: int):
    """计算输入的整型的1024幂"""
    time.sleep(2)
    return a ** 1024


print(f1(2))


@timer
def f2(dic: dict):
    """交换字典的key、value"""
    dic1 = {}
    for key, value in dic.items():
        if not isinstance(value, list) and not isinstance(value, dict):
            dic1[value] = key
        else:
            return '可变序列不可作为字典的key'
    return dic1


print(f2({'name': 'chaizhenhua'}))
