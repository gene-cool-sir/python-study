# --coding:utf-8--
# key：value键值对; 字典依靠key，列表依靠索引
info = {'name':'gene','age':18}
print(info)
print(info['name'])

#生成字典的方式
dic = dict(x=1,y=2)
print(dic)
# 直接赋值一个不存在的key:value
dic['d']='d'
print(dic)

# 字典在添加的时候是可以的，是可变类型
# 列表添加和修改必须通过存在的索引
# 字典的len查看键值对的个数
print(len(info))

# 成员运算in 和 not in 字典的成员运算判断的是key 返回的是布尔值
print('gene' in info)
print('age' not in info)

# del 删除
del info['name'] # 删除不存在的key会报错

#clear
info.clear()
print(info)

# pop 删除 返回的是value
dic.pop('d')
print(dic)
# pop('xx') 不存在的key会报错
# popitem 最后一对键值对删除，字典无序 ， 返回的是一个元组

info1 = {'name':'gene','age':18}
res1 = info1.popitem() # 字典中不存在元素的时候会报错
print(res1)
print(info1)

# 修改， update
info1.update({'name':'gene3'})
print(info1)

# setdefault : key存在则不重新设置值，字典key不存在则新增key:value
res2 = info1.setdefault('name','g')
print(info1)
print(res2)
info1.setdefault("sex",'male')
print(info1)

# 查
print(info1['name'])  #key不存在，会报错
print(info1.get('name'))   # 当key不存在不会报错

# 取出所有的key
print("------------")
print(list(info1.keys()))
# 取出所有的values
print(list(info1.values()))
# 取出所有的键值对
print(list(info1.items()))
