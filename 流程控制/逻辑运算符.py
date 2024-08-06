# 逻辑运算符 and or not
# and 左右条件都为真才为真
name = "haha"
age =20
print(age > 18 and name == 'haha')

# or 左右条件只要有个为真就是真
print(age > 21 or name =='haha')

# not 非 否定
print(not age > 21)

'''
原理： 
1. not的优先级最高，not与紧跟其后的条件不可分割
2. 如果语句中全是and连接，或者or连接，则从左到右一次计算
3. 如果语句中有and 和or ， 那么先括号把and的左右2个条件括起来，在进行运算
'''
print(not 3 > 1 or  3> 2) # 会先判断 not 3 > 1 而不是 3>1 or 3 >1
# not 相当于乘除法， and or 相当于 加减法
res  = not False and True or False or False or True
print(res)
# 最好使用括号来区别优先级，
res1 = (3>4 and 4 >3) or (1 ==2 and 'x' == 'y')
print(res1ß)