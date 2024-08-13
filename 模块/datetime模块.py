# -*-coding:utf-8-*-
'''
 datetime： time用起来不方便， datetime更加灵活和本地化
'''

from datetime import datetime
# 获取时间， 获取当前时间，并返回格式化字符串
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.microsecond)
# 手动指定时间
dt = datetime(2024, 4, 19, 12, 20)
print(dt)
#
c = dt - datetime.now()
print(c)

# 替换某个时间单位的只
print(dt.replace(year=2025))
