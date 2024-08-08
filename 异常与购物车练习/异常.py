#-*-coding:utf-8-*-
''''
1. 异常：
 异常是错误发生的型号， 没有被应用程序处理，就会抛出异常，程序终止运行
 异常包含3部分
 - 异常追中信息
 - 异常的类型
 - 异常的信息
 错误的分类：
 - 语法错误： 在程序运行之前可以立即修正，好避免
 - 逻辑上的错误： 程序运行中出现的错误，不能立即修正
异常的处理： 避免程序因异常崩溃。
语法：
try:
    code1
exception NameError:
    code1
exception ...:
    code2
else:
    xxx
finally:
    xx
'''

import inspect
# 异常处理单分支
try:
    a
except NameError as e:
    print("请检查代码")
    print(e)
else:
    print("代码正确")
finally:
    print("完成了代码捕获，最后我会执行")

# 常见异常
'''
NameError
TypeError
SyntaxError
KeyError
IndexError
'''
# 异常处理多分支
try:
    l = [1, 2]
    l[3]
    print("=============>异常了，我还执行吗")
except (NameError, KeyError) as e:
    print("请检查代码")
    print(e)
except IndexError as e:
    print(e)
else:
    print("代码正确")
finally:
    print("完成了代码捕获，最后我会执行")

# 万能捕获异常


try:
    d={'x':1}
    d['y']
except Exception as e:
    print("什么异常都可以捕获", e)
else:
    print("没有异常")
finally:
    print("捕获OK")

# 判断文件是否存在
try:
    f = open('tex1.txt','r')
except:
    print("文件没有创建")
    # f=open('text1.txt','w') # 没有我会创建一个文件
else:
    print(f.read())
finally:
    if 'f' in locals() :
        f.close()

# 断言
print('-=----------------------------')
# 自定义异常
l = [1,2,3,4]
#if len(l) != 5:
 #   raise TypeError('列表长度必须为5')
assert len(l) == 4 # 断言错误

# 报错的情况下进行文件关闭



