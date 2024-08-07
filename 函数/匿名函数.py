# -*-coding:utf-8-*-
'''
匿名函数： 没有名字的函数
使用： 临时使用一次，没有重复使用的需求
语法： lambda空格 + 参数 + 函数体代码 lambda x,y: x+y
调用：内存地址加括号   (lambda x,y: x+y)(1,3)   lambda表达式本省 + （参数）
返回值省去了return

'''
# 匿名函数
print((lambda x,y: x+y))
print((lambda x,y: x+y)(1,3))

# 函数的形式
print((lambda x, y: print(x + y)(1, 5)))
f = lambda  x,y: x+y
print(f(2,3))

# 匿名函数与内置函数结合使用

#max min, sorted
ss = {
    'haha':3300,
    "xisi":55,
    'dada':6600
}
# 默认比较key的值
print(max(ss))

# 按照value 值比较 max(字典，key=函数名）
def func(name):
    return ss[name]

print(max(ss, key=func))

print(max(ss, key=lambda name: ss[name]))
print(min(ss, key=lambda name: ss[name]))


ages =[22,11,44,9,1]
print(sorted(ages, reverse=True))

# for循环遍历
for i in ages:
    print(i)

print(sorted(ss, key=lambda name: ss[name], reverse=True))
print(sorted(ss, key=lambda name: ss[name], reverse=False))
print(sorted(ss, key=lambda name: name, reverse=False))


