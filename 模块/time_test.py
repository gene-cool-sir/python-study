# -*-coding:utf-8-*-
'''
time模块： 与时间相关的功能
时间分3种：
1.时间戳： timestamp,从1970.1.1 00:00:00开始计算的秒数，主要用于计算两个时间的差
2.localtime: 本地时间，表示计算机当前所在位置
3.UTC: 世界协调时间，表示UTC时间，表示协调世界时，1970.1.1 00:00:00

'''
import time
# 获取时间戳， 返回浮点数
print(time.time())
# 获取本地时间，返回结构化时间
print(time.localtime())
# 获取UTC时间，返回结构化时间， 比中国时间少8小时
print(time.gmtime())
# 结构化时间转换为字符串时间
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# 将格式化时间转换为结构化时间
print(time.strptime('2018-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

# 时间戳转结构化
print(time.localtime(time.time()))
# 结构化转时间戳
print(time.mktime(time.localtime()))
# sleep函数
time.sleep(2)
print('hello world, over')

