# --coding:utf-8--
'''
s1 = {'ab','c'}
s2={'d','c','f'}
print(s1 & s2) 交集
print(s1 | s2) 并集
print(s1 - s2) 差集

'''
# 每一个值都必须是不可变类型
# sss={'abc','def',{'a','b'}} eoor

s = {'ab','c','d','f'}
# 增加
s.add('e')
print(s)
# 删除， pop, 从第一个元素开始删
s.pop()
print(s)
# 指定删除remove
s.remove('c')
print(s)
# 改 update
s.update(['haode'])
print(s)

# 变列表
print(list(s))

# 转回为set 集合
arr=['a',1,2]
print(arr)
print(set(arr))

# 集合去重 1.无法保证元数据的顺序，2当某个数据中包含的多个只全部为不可变的类型的时候才可以用集合去重
names=['haha','gege','gege','gene','gene']
na_s = set(names)
print(na_s)
l = list(na_s)
print(l)

