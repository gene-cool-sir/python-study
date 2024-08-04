# --coding:utf-8--
L=['dahai','abc',["aa",'def']]
# 改掉数组值，如果是字符串的取值不可修改
L[0]='hehe'
print(L)
print(L[0:2:1])
# len长度
print(len(L))
# 查看列表中元素个数
print(L.count("aa"))
# 成员 in 和 not in
print('abc' in L)
print('' not in L)
# 在列表中从左到右查找指定的元素，找到了返回值的下标、索引
print(L.index('abc'))

# append 向列表末尾追加一个元素
L.append("world")
print(L)
# 规律列表的修改和新增都不需要重新赋值，是可变类型； 字符串、数字、布尔、复数是不可变类型
# extend() 向列表中添加多个元素， 括号里面放列表，也是末尾追加
L.extend(['extend1','extend2'])
print(L)
# insert(索引，元素）向指定缩影位置前插入一个元素
L.insert(1,"insert1")
# 删除
del L[0]
# 指定删除
L.remove('abc')
print(L)
# pop 从列表删除并返回， 默认删除最后一个元素， 可以通过索引删除
L.pop()
print(L)
L.pop(0) # 删除返回指定索引值，没有返回None
print(L)
# 反序
L.reverse()
print(L)
# 清空列表 clear
L.clear()
print(L)

sort_num=[1,2,3,4,5]
# reverse=True 是倒序；reverse=False 是正序
print(sort_num.sort(reverse=True))
print(sort_num.sort(reverse=False))


