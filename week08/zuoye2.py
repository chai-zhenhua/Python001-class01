"""
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
"""

def map(func, iter):
    for n in iter:
        yield func(n)

def f1(n):
    return n * n

l1 = [1,2,3,4,5,6, ]

ret = map(f1,l1)
print(list(ret))