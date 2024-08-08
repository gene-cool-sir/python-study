# -*-coding:utf-8-*-
'''
f.seek
文件内指针的移动，只有t模式下的read(n), n代表的字符个数；  b模式下：指针的移动都是以字节为单位

指针操作f.seek(offset,whence)
offset: 指针移动的字节数
whence: 代表惨遭什么位置移动
    0：  参照文件的开头（默认值）， 可在t和b模式  eg: 'ab红黑'  f.seek(2,0) 代表从文件开头，移动2个字符，从第三个字符开始读后面， f.read(1) 那么读取到的一个字符就是’红‘
    1： 参照当前所在位置， 必须在b 模式 f.seek(1,1), f.tell() 获取当前光标位置， 然后跳过1个字符， 读取后面的字符
    2： 惨遭文件末尾， 必须在b模式： f.seek(0,2), 这是在文件的末尾； f.seek(3,2), 文件末尾向前3个字节， f.read(3) 读取到的是‘黑’
'''
# t 模式
with open('test.py', mode="rt",encoding='utf-8') as f:
    print(f.read(1))
    print(f.read(3))

# b 模式
with open('test.py', mode='rb') as f:
    print(f.read(1).decode('utf-8')) # 读取1个字节， # 在utf-8 中是一个字节， 1个汉字是3个字节， 需要注意
    f.tell() # 查看当前光标位置

