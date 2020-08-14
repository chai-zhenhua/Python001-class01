"""
作业二：
自定义一个 python 函数，实现 map() 函数的功能。
"""

# def map(func, iter:iter):
#     result = []
#     for n in iter:
#         c = func(n)
#         result.append(c)
#     return result
#
def f1(a):
    return a ** 2

l1 = [i for i in range(1,11)]

# d = map(f1, l1)
# print(d)
d = map(f1,l1)
print(list(d))


