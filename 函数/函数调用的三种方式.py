# -*-coding:utf-8-*-
# 语句形式
'''
def foo():
    code1
foo()
'''

# 表达形式
def foo(x,y):
    res = x + y
    return res
res = foo(1, 2) * 100
print(res)

# 可以当作参数传递给另外一个函数
def max2(x, y):
    if x > y:
        return x
    else:
        return y

print(max2(1,2))
# 传递函数
print(max2(max2(1,2), 5))


