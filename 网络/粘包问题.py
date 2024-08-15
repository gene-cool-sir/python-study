# -*-coding:utf-8-*-
'''
收发消息多
'''
# data = conn.recv(1024)   # 一次性接收1024字节

# 接收端保证100%接收到数据
'''
粘包问题 ： 是TCP协议流式传输的方式导致的
解决： 接收端能够精确的接收每个数据包
客户端： 告诉服务端发送多少数据，就有多少个报头

报头： 应该包含信息：数据长度信息
问题：
    1. 发送的数据只能byte类型； 描述长度的是数字，应该吧整形数字转换为固定的byte类型
    
struct模块

 '''
import struct

# 把数字转换为4个bytes
obj = struct.pack('i', 10000)
print(obj, len(obj))

# 把byte类型转为数字类型
res = struct.unpack('i', obj)
print(res, res[0], type([res[0]]))
