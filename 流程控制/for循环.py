# for 循环
'''
按照索引顺序遍历
for n in names:
    print(n)

'''
names = ['ge', 'da', 'he', 'hei']
for i in names:
    print(i)

# for 循环遍历set
keys = {'ke1', 'ke2', 'ke3'}
for i in keys:
    print(i)

print("==============")

# for 循环遍历字典
key_values = {'name1': 'value1', 'name2': 'value2'}
for i in key_values:  # 默认遍历keys
    print(i)

print("==============")
for i in key_values.keys():
    print(i)

print("==============")
for i in key_values.values():
    print(i)

print("==============")
for i in key_values.keys():
    print(key_values[i])

print("==============")

# 遍历键值对
for i in key_values.items():
    print(i)
    i_set = set(i)
    for j in i_set:
        print(j)
print("==============")

# for循环次数是有被循环对象包含值的个数决定的； while的循环次数是有条件决定

# range(起始索引，结束索引，步长）； range(结束索引，步长） 起始索引相当于0
a = range(0, 5)
print(a)
print(type(a))

# 它是一个迭代器
print(list(a))  # 不直接使用列表，这样可以节省内存
for i in range(0, 5):
    print(i)
print("==============")
