# -*-coding:utf-8-*-
# 将文件内容由硬盘全部读入内存；  在内存中完成修改，将内存中修改后的结果覆盖写回硬盘
with open('test.py', mode='rt', encoding='utf-8' ) as f:
    all_data=f.read()
    print(all_data)

# 读出来的数据已经存到all_data变量中了
with open('test.py', mode='wt', encoding='utf-8') as f:
    f.write(all_data.replace('world','hello hello world'))

# replace 字符串替换：
a='abcHAHA'
print(a.replace('abc', 'def'))

# 文件修改方式二： 以读的方式打开源文件，以写的方式打开一个临时文件； 从源文件中读内容修改完成后写入临时文件，直到源文件读取完毕； 删掉源文件，将临时文件重命名为源文件
import os
with open('test.py', mode='rt', encoding='utf-8') as read_f, open('temp.py',mode='wt', encoding='utf-8') as write_f:
    for line in read_f:
        print(line)
        write_f.write(line.replace('hello','hi'))
# 移除源文件
os.remove('test.py')
# 改名
os.rename('temp.py','test.py')

# 方式一： 内存操作，占用内存大； 方式二： 硬盘会临时多出一个文件，操作完后进行删除
