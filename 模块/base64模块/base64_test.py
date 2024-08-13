# -*-coding:utf-8-*-
'''
Base64是网络上最常见的用于传出8bit字节码的编码方式之一；
Base64是一种在因特网上传送邮件的编码方式，通过Base64编码后的数据可以以8bit为单位被传送；基于64个可打印字符来表示二进制数据的方法
定义： 8bit字节代码的编码方式之一
可用于： 在HTTP环境下传递较长的标识信息
特性： Base64不具有可读性
# Base64只用于传输，并不加密
原理： 字符引用了 [A-Za-z,0-9,+,/] 64个可打印字符
数值代表字符的索引，这是Base64编码的协议规定的不能更改
'''

import base64
a = '大人'
b = base64.b64encode(a.encode('utf-8'))
print(b)
# 将base64编码的bytes数据解码成字符串
c = base64.b64decode(b).decode('utf-8')
print(c)
