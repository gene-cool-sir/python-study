#tab缩进代码， 在if 代码块只有一行的时候，还是很有用的
'''
1.语法：
if 条件
    代码体
# 记忆方法
    if + 空格 + 冒号
    tab缩进代码
'''

tag = True
if tag:
        print("条件")
        print("条1")

# if  else 语法
tag1 = 1==2
if tag1:
        print("tag条件不满足")
else:
        print("tag1条件不满足")

# 多分支 if 条件1： elif: 条件2  elif: 条件3 else: 条件4
#score = int(input("》》》"))
score = 80
if score > 90:
        print(score)
elif score >= 80:
        print("80-90")
elif 70 > score > 80:
        print("70-80")
else:
        print("60 ")

# elif 与if的区别
# if 并列是每个if都是独立的； elif的条件是上一个if 或者上一个elif 不满足条件向下执行的条件

# 3. if 嵌套语法
'''
if 条件1：
        code
        if 条件2：
        code2
'''
cls = 'human'
sex = 'female'
age = 20
if cls == 'human' and sex == 'female' and age > 18 and age < 26:
        print("开始对了")
        new= '新开始'
        # 嵌套里面是用if语法。。。 elif 中也可以， else： 中也可以； 他们都是做为了一个内部模块在其中继续进行分支代码
        if new == '新开始':
                print(new + "继续")
        else:
                print("开始后结束了")
else:
        print("直接结束了")

#





