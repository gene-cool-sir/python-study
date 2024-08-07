# -*-coding:utf-8-*-
'''
 装饰器： 就是一个函数，不是给自己使用，而是给其他函数添加功能； 装饰值的是为被装饰的对象添加额外的功能
 1. 为什么使用装饰器？
    软件的封闭原则：

实现： 通过闭包函数的方式来增强， 把普通函数作为参数进行传递，然后在闭包函数内进行增强，进行装饰。
'''


def run(name):
    print("跑步" + name)


def fitness(name):
    print("健身" + name)


name = "dahai"


def decorate(func):
    def new_func(name):
        print("我是装饰前的代码")
        func(name)
        print("我是装饰后的代码")

    return new_func


run = a = decorate(run)
run('ahha')

# for循环从1-900000

n = 9000000

from datetime import datetime


def run_time(func):
    def new_func(*args, **kwargs):
        start_time = datetime.now()
        print("开始时间：%s" % start_time)
        func(*args, **kwargs)
        end_time = datetime.now()
        print("结束时间：{}".format(end_time))
        time1 = end_time - start_time
        print("花费时间：%s" % time1)

    return new_func


# 定义装饰函数， 在run_time 之后定义
@run_time  # 装饰函数for1 ， 等同于 for1 = run_time(for1)； 使用这种方式装饰函数run_time在前，被装饰函数在run_time之后
def for1(n):
    sum1 = 0
    for i in range(1, n + 1):
        sum1 += i
    print(sum1)


for1(n)  # 通过@run_Time 装饰后， 直接可以调用源函数， 就是装饰后的函数了
