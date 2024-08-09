# -*-coding:utf-8-*-
'''
生成器： 是一种自定义的迭代器
函数内包含yield关键字，调用函数不会执行函数体，而是返回一个生成器对象
对于生成器来说，生成器对象本身就是迭代器。gen is gen.__iter__().__iter__() # True
迭代器的迭代器是它本身， True

yeild 可以报错函数的暂定状态
yeild 与 return 的 区别：
相同点：都是返回值，但是return会退出函数，yeild会暂定函数
不同点：yeild可以返回多次值，return只能返回一次值

'''
def func():
    print('start')
    yield 1
    print('continue')
    yield 2
    print('end')
    return 'over'
gen = func()
print(gen)
# 对于生成器来说，生成器对象本身就是迭代器。这意味着如果你有一个生成器对象 gen，那么 gen 和 gen.__iter__() 返回的是同一个对象，因此 gen is gen.__iter__() 会返回 True。
print(gen is gen.__iter__().__iter__())
print(gen is gen.__iter__())
# next(gen) 触发函数体的执行， 直到遇到yield关键字， 并将yield后面的值返回
print(next(gen))
print(next(gen))


# 定一个生成器，生成10位的斐波拉契数列 【0,1,1,2,3,5,8,13,21,34]
#  i 是计数循环， a 是当前数， b 是下一个数, n 是循环次数
def fib(n):
    i, a, b = 0, 1, 1
    while i < n:
        yield a
        a,b=b,a+b
        i+=1

run = fib(10)
print(list(run))
print('-----------------------')
for i in run:
    print(i)

# 函数不能不断传值， 生成器可以（yeild） x = yield
def fun1(n):
    food=[]
    while True:
        food1=yield food
        print(food1)
        food.append(food1)

g = fun1('hi')
print(next(g))
# send(food1) 将 food1 传给 yield food， 生成器直到遇到 下一个yield 停止，将 food1 赋值给 food， 并将 food 返回
g.send('hello') # 将 hello 传给 food1， 并调用next()打印 food1, 并且返回 food
g.send('world')
print(g.send('python'))


# 用生成器计算1+2*2+3*3+4*4+5*5的和
def sum_factorial(n):
    i, a = 0, 1
    while i < n:
        yield a
        i += 1
        a = (i+1)*(i+1)

factorial = sum_factorial(5)
print(list(factorial))

factorial = sum_factorial(5)
sum = 0
for i in factorial:
    sum += i
print(sum)


