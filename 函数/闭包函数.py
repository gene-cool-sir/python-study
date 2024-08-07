# -*-coding:utf-8-*-
'''
闭包：
1. 改函数是一个内部函数
2. 改内部的函数名字在外部被引用
3.

'''
def outer(): # 没有调用outer(),但是创造了outer这个函数
    print("外面的函数正在运行")
    def inner():
        print("内部函数在运行")
    return inner # 当使用return 返回内部函数的时候， 内部函数才可以被外部调用

outer() # 调用外部函数的时候，才会创造内部的inner() 函数，  inner() 函数不能直接在外部被调用

innter =  outer() # 使用return 返回了inner函数，外部可调用
innter()


# 函数传参数方式： 闭包; 当不想让外界知道内部传递了什么参数， 则可以使用闭包， 返回一个内部函数，直接调用内部函数