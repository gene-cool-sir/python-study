# -*-coding:utf-8-*-
# from 模块名 import 各种名字变量名，函数名等

from spam import money,read
print(money)
print(read())

# * 代表导入模块中所有的名字
from spam import  *

# 起别名
from time import thread_time as time1
print(time1())

# from 文件夹 import 模块名
# 绝对路径
from dir import m1
m1.f2()

# 相对导入
'''
from  .文件夹 import 模块
from ..文件夹 import 模块

相对导入： 惨遭当前文件的文件夹为起始查找
符号： . 代表当前文件的文件夹。 .. 代表上一级文件夹 ，一次类推
优点： 导入更加简洁
缺点： 只能导入包中的模块时才能使用，不能再执行文件中使用

'''

# 无前缀导入
# from dir.m1 import f2