# -*-coding:utf-8-*-

import socket
# 买手机,SOCKET_STREAM TCP流式协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)

# 插手机卡
phone.bind(('127.0.0.1',8080))

# 开机
phone.listen(5)

#等待请求
print('start')
conn,client_addr = phone.accept()
# 建立3次握手
print(conn,client_addr)

# 接收客户端请求
data = conn.recv(1024)
print('收到客户端数据：' + data.decode('utf-8'))
# 发送数据
conn.send(data.upper())

conn.close()
phone.close()

