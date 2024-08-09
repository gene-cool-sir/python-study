# -*-coding:utf-8-*-
# 乱码
with open('test.py', mode='r', encoding='utf-8') as f:
    print(f.read().encode('utf-8'))

# 包装不乱码： 字符按照什么标准进行编码，就按照什么标准解码
# 在内存中写的所有字符，都是一视同仁，都是unicode编码； 挡在写入硬盘或者网络传输的时候才会转换为对应标准的编码格式
