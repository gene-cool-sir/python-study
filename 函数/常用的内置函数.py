# -*-coding:utf-8-*-
# 已经写好的函数
# 绝对值
print(abs(-5))
print(abs(5))

# all(可迭代的对象) 返回值是布尔值
# 可迭代对象黎明的只全为真为真，其余为假
# 可迭代对象是空为真

print(all([1,'',None]))
print(all([1,'aa',2]))
print(all([]))

# any(可迭代对象)
# 返回值全为假则为假，其余为真
# 可迭代对象为空为假
print(any([1,'',None]))
print(any([1,'aa',2]))
print(any([]))

# 求最大值
a = [1,2,3,4,5]
print(max(a))

# 最小值
print(min(a))
#求和
print(sum(a))

# ascll 英文字符编码：
# ord() 可以把字符串转为编码
# ch让()  可以把编码转换为字符
print(ord('a'))
print(chr(97))
print(ord('b'))

# 拉链函数 zip, 按照索引进行匹配，进行匹配，把值拉在一起
t1 = ['a','b', 'c','d']
t2 = [1,2,3,4,5]
# 通过索引
print(zip(t1,t2))
print(list(zip(t1,t2)))
print(dict(zip(t1,t2)))
print(set(zip(t1,t2)))

# exec 函数， 可以执行字符串里面的代码; 支持Python语法
exec('print(1)')
exec('''
for i in range(1,5):
    print(i)
''')
