# -*-coding:utf-8-*-
import spam
# 调用模块中的方法，模块名.方法名
print(spam.read()) # 读取内容
'''
 import 导入模块： 在使用时必须要导入模块，才能使用模块中的方法： 前缀：模块名
 优点： 有命名空间，不会与当前命名空间中的变量名冲突
 缺点，但凡导入模块中的名字都需要加前缀，不够简洁
'''
import time
print(time.time())

# 给模块取别名
import time as mytime
print(mytime.time())