# -*-coding:utf-8-*-
'''
r+t: 可读写，比rt 多一个末尾写
w+t: 可写读， 比wt多一个读， 可通过seek,
a+t: 可读写， 在多次打开open,会追加
'''

with open('test.py', mode='r+t', encoding='utf-8') as f:
    f.write("# world")
    f.seek(0,0) # 指针移动seek(移动的字节数,开头开始)
    print(f.readline())
