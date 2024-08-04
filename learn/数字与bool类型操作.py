# --coding:utf-8--
# 赋值运算 = += -= *= /= %= **= //=(地板除赋值）
#语法 n = n +xx
n = 5
n += 1
print(n)

# 布尔类型
'''
所有的数据类型都自带布尔值
1. None ，0，空（空字符串，空列表，空字典）三种情况的不认字都为False
2. 其余值都为真
'''
tag1 = None
tag2 = []
tag3 = ""
tag4={}
tag5={'nihao','feichanghao'}
print(bool(tag1))

if tag1 or tag2 or tag3 or tag4:
    print("数据类型自带为True-tag")
elif tag5:
    print("数据类型自带True- {0}".format(tag5))
else:
    print("数据类型自带False")