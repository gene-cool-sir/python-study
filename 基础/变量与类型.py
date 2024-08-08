# --coding:utf-8--

'''
1.为什么要使用变量： 计算机可以将一个事务的特征或者状态记录下来（存储于计算机），使用的时候可以取出
2. 如何使用变量
  见名知义； 变量名第一个字符不能是数字
  变量名只能是字符数字和下划线任意组合的字符串
  下划线、驼峰
  常量：是全部大写，变量不可变，可以改（通常用大写来表示）
'''

# 变量的语法
name = 'door'
# 变量名： 相对于一个表示； = 是赋值
# 变量使用
print(name)
# id相当于在内存中的位置或者地址
print(id(name))

# 类型
'''
1. 引号：可以是单引号、双引号、三引号
'''
name1="door1"
print(name, name1)
# 字符串可以相加
print(name + "hello")
# 索引： 从0开始
print(name[0])
print(name[-1])

# 输入与输出
'''
1. print 输出
2. input输入： input(提示用户输入信息）输入的数据都会变为字符串
'''
# name2 = input(">>>")
name2 = "print"
print(name2)
print(type(name2))


# 字符串类型格式化输出
'''
1. 占位符： %s 、 %d
'''
# 单个值，通过%接收值
print('my name is %s' %name)
# 多个只，直接放到%后需要括号
print('my name is %s, age is %d' %('gene', 16))

# 数字类型
'''
1. int类型，定义： age=18
2. float类型，定义： weight=119.8； print(type(weight))

'''

# 算术运算
'''
加 + - * / %  **(乘方）
'''
print(7//3) #取整
print(3**2) #9

# 比较运算符
'''
!= > < >= <=   返回值是True 或者False
'''
# 布尔类型
'''
True 
False
判断条件成立 True， 判断条件不成立 False
'''
tag = True
print(type(tag))

# 复数类型
x = 1 -2j
print(type(x))

# 列表
'''
list： 记录或者存储多个值；定义： [] 内逗号分割多个任意类型
'''
L = ['door',name, 1, 1.2]
print(L)
# 索引是从0开始
print(L[0])
print(L[-1])  # 反向取

# 字典
'''
dict： 作用是记录多个key：value值； 
定义： 在{}内用逗号分隔多个key：value元素；value可以是任意类型数据，key通常是字符串类型
'''
info = {'name':'door', 'age':18}
print(info['name'])

# 元组
'''
tuple: 用途，记录多个值，当多个值没有更改的需求，此时适合元组
定义：在()内用逗号分隔开多个任意类型的值
'''
t=(1,2,('haha'),['ni','hao'])
print(t[3][1])

# set
'''
用途：关系运算
定义： 在{}内用逗号分开多个值
元素不能重复且无序
'''
s={'a','b','c'}
s2={'a'}
print(s & s2) # 2个集合相同的元素
print(s2 | s2) # 2个集合并集
print(s2 - s2) # 2个集合的差集
print(s2)

# 一个值： 字符串、数字、布尔、复数
# 多个值： 有序的列表、元组（不能修改） 、无序的字典、集合（关系运算）








