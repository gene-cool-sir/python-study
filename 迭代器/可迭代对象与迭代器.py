# -*-coding:utf-8-*-
'''
1. 什么是迭代器 ： 迭代就是更新迭代
 1. 迭代器： 迭代取值的工具
 2. 迭代是一个重复的过程，每次重复都是基于上一次的结果

'''
# 单纯的循环， 没有基于上一次的结果： 不算迭代

# 迭代
L = [1, 2, 3, 4, 5]
i = 0
while i < len(L):
    print(L[i])
    i += 1
# 那些数据类型需要（可以）迭代取值
# 字符串 、 列表、 元组、 字典、 集合、 文件等

# 迭代器提供了一种不依赖索引迭代取值的功能
# 每个需要取值的都加了 __iter__方法
a = 1
# a.__iter__() 没有
c = 'hell0'
c.__iter__()  # 存在  如果有__iter__方法，就表示可以迭代取值

# 迭代器： 执行可迭代对象下的__iter__方法，返回一个迭代器对象
dic = {'a': 1, 'b': 2}
# 可迭代对象变成迭代器
iter_dic = dic.__iter__()
print(iter_dic)
# 迭代器有一个__next__方法，每次调用都会返回一个值
print(iter_dic.__next__())
print(iter_dic.__next__())  # 默认遍历的就是key # StopIteration 是一个结束信号，代表迭代器取完了

# 列表不依赖索引取值
l = [1, 2, 3, 4, 5]
iter_l = l.__iter__()
print(iter_l.__next__())
print(iter_l.__next__())
# 误区
print(l.__iter__().__next__())  # 每次迭代都会重新创建迭代器
print(l.__iter__().__next__())  # 每次迭代都会重新创建迭代器

# 可迭代对象： 只有__iter__方法，没有__next__方法; 迭代器： 有__iter__和__next__方法;
# 可迭代对象的数据类型： 字符串、列表、元组、字典、集合、文件等； 迭代器的数据类型： 迭代器、生成器、生成器表达式
# 迭代器有内置的__next__方法，z执行迭代器的时候，会调用__next__方法，返回一个值，可以不依赖索引取值
# 迭代器有内置的__iter__方法，执行迭代器的时候，会调用__iter__方法，返回迭代器本身，可以不依赖索引取值
# 迭代器一定是可迭代对象，可迭代对象不一定是迭代器；可迭代对象只需要有__iter__方法，迭代器需要有__iter__和__next__方法

# 案例
l2 = [1, 2, 3, 4, 5]
iter_l2 = l2.__iter__()

print(l2 is l2.__iter__(),'==============') # False
# 调用可迭代对象的__iter__方法，返回迭代器
print(iter_l2 is iter_l2.__iter__())  # True 执行迭代器的时候，会调用__iter__方法，返回的是迭代器本身
# 作用： for 循环

# 原生方法 iter() next()
dic2 = {'a': 1, 'b': 2}
iter_dic2 = iter(dic2)
print(iter_dic2)
print(dic2.__iter__())
print(next(iter_dic2))
print(iter_dic2.__next__())

# 解决迭代器报错
while True:
    try:
        print(iter_dic2.__next__())
    except StopIteration:
        print('迭代结束')
        break

print('==============')

while True:
    try:
        print(next(iter_dic2))
    except StopIteration:
        break

# 迭代器： 迭代取值的工具, 可迭代对象变成迭代器，能够自己获取迭代器对象next的值， next 最后不报错
# for 本质上是迭代器循环： 先调用in后面的可迭代对象的__iter__方法，返回迭代器对象，再调用迭代器的__next__方法，返回迭代器的值，直到迭代器取完
# 调用 next(), 将得到的值赋值给变量，循环执行，直到迭代器取完
# 循环直到next()抛出StopIteration异常，表示迭代结束，for 会自动捕获这个异常，结束循环
for i in dic2:
    print(i)

'''
迭代器总结： 
1. 优点：提供了一种通用的且不依赖索引的取值方式，同一时刻在内存中只存在一个值  
2. 缺点： 不如直接按照索引取值灵活，无法预测迭代的长度
'''

# 模块
from collections import Iterable  # 迭代对象
from collections import Iterator  # 迭代器

l3 = [1, 2, 3, 4, 5]
#print(isinstance(l3, Iterable))
print(isinstance(l3, Iterator))
