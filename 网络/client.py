# -*-coding:utf-8-*-
import socket
# 买手机,SOCKET_STREAM TCP流式协议
phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(phone)

# 拨号
phone.connect(('127.0.0.1', 8080))

# 发消息, 二进制传输
#phone.send(b'hello')
phone.send('world'.encode('utf-8'))
#phone.send(b'exit')
# 接收消息
data = phone.recv(1024)
print('接收消息:' + data.decode('utf-8'))

phone.close()