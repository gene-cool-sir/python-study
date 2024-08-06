# -*-coding:utf-8-*-
# 外部不能访问函数内部的变量
def fun1():
    x =1
#print(x) # 报错

# 函数内部可以访问防暑外部的变啊领
x=123
def fun2():
    print(x) # 函数里面可以访问，但是不能直接修改函数外的变量
fun2()

# global 能让我们在函数里面修改全局变量的值

def fun3():
    global x
    x = x + 1

fun3()
print(x)

# 可以让签到函数能修改嵌套函数之外的值, 不使用global, 使用nonlocal
def fun4():
    b = 100
    def fun5():
        nonlocal b  #  嵌套函数内不适用 global b
        b += 1
        print(b)
    fun5()
fun4()
