# -*-coding:utf-8-*-

# 什么是返回值
L = [2, 3, 4]
n = L.pop()
print(n)
for i in L:
    print(i)

'''
1. return: 是函数结束的标志，函数内可以有多个return；但只要执行一次，整个函数都会结束； 默认return 返回None
2. return 返回值无类型限制， 可以是任意类型的数据
3  return 返回没有个数限制， 可以用逗号分隔开多个任意类型的只
    0个： 返回None， 不写return 默认会在函数的最后一行添加 return None
    1个： 返回值就是这个值本身
    多个： 返回值是yuanzu
4  return 关键字是函数结束的标志，可以利用这一点结束循环

'''


def factory(a):
    print(a)
    print("zhizao")
    return 'h' + str(a)


re = factory(1)
print(re)


def factory(b):
    print(b)
    return [1, 2, 3], 'a', True


re1 = factory('abc')
print(re1)

# return 函数结束
def factory(c):
    while True:
        if c ==1:
            print('结束了。。')
            return
        c +=1
        print(c)

factory(1)



