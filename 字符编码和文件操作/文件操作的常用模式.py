# -*-coding:utf-8-*-
'''
1. 文件的打开模式
 r : 只读模式
 w:  只写模式
 a: 只追加写模式

2. 控制读写文件单位的方式（必须与r/w/a连用）
    t: 文本模式，一定要指定encoding 参数； 优点： 操作系统会将硬盘中的二进制数字解码成unicode然后返回； 强调只针对文本文件有效
    b: 二进制模式，一定不能指定encoding参数； 优点：

'''

# r: 只读模式； 当文件不存在时，会报错；当文件存在时，文件指针指向文件的开头
with open('文件.py', mode='rt', encoding='utf-8') as f:
    #print('>>>>',f.read())
    #print('第一次读完了')
    #print('2',f.read())
    print(f.readable())  # 判断模块只读
    print(f.writable())  # 判断模块不可写
    print(f.readline(), end='')  # end 是print 默认值是换行服， ‘’ 设置不换行
    print(f.readline())
    #for line in f:
    #   print(line, end='')
    #for line in f:
    #    L.append(line)
    #print(L)

    # 一行读取所有
    print(f.readlines())

# wt: 只写模式
# 当文件不存在时， 报错
# 文件存在时， 文件指针指向文件的开头
with open('文件.py', mode='wt', encoding='utf-8') as f:
    print(f.writable())

# 当文件不存在时，新建一个空文件
with open('test.py','wt',encoding='utf-8') as f:
    f.writable()
    f.write('hello world')
    f.writelines(['aba\n','def']) # 再次写入，会覆盖源文件内容 mode=wt , mode=at 是追加

with open('test.py', mode='at', encoding='utf-8') as f:
    print(f.writable())
    f.write('zhuijia')
    f.write(' ok~')

# 当文件存在时，清空文件内容， 文件指针跑到文件开头
with open('test.py', mode='wt', encoding='utf-8') as f:
    pass
# 在每次open后，  wt 会覆盖文件内容，重新写， at 会追加

# 二进制文件 b 模式
# 图片或视频
with open('springmvc.png', mode='rb') as f:
    data=f.read()
    print(data)
    print(type(data))

with open('spring.png',mode="wb") as f:
    f.write(data) # copy

# 用b模式，也可以对文件文件操作，但是要解码
# decode 二进制解码成字符   encode 字符编码为二进制
with open('test.py',mode='wb') as f:
    f.write('# hello'.encode('utf-8'))

with open('test.py', mode='rb') as f:
    data = f.read()
    print(data.decode('utf-8'))

















