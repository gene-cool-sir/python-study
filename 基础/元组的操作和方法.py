# --coding:utf-8--
# tuple 元组中的元素是不可更改的，如果元组中的元素是可变类型，那么可以修改元组中可变元素内部的值
t=('a','b',('c','d'),['e','for'])
# t[0]='aa'  # error
t[3][0]='d' # 修改可变类型中的元素
print(t[3][0])
 # t[4]=1 # 不支持
#元组是不能修改和添加， 所以元组是不可变类型
# 修改元组， 转换为列表
t1=list(t)
print(t1)

t1.append('append')
print(t1)
# 列表转换为元组
t= tuple(t1)
print(t)
# 查： 与列表一样索引、切片、长度len、count个数、index查找元素所在位置，成员运算
