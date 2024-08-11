# -*-coding:utf-8-*-
'''
1.初始化：
    以双下划线开头且以双下划线结尾的固定方法，他们会在特定的时机会被触发执行，
    __init__ 它会在实例化之后自动被调用， 以完成实例的初始化
'''

class Teacher:
    # 属性、特征
    school = '成都川大' # 类中的属性，所有对象都有
    def __init__(self,name,age,sex): # self 会自动传递， 其余为形参属性
        print('初始化')
        self.name = name
        self.age = age
        self.sex = sex

    # 函数
    def course(self,name):
        print('上课')
        # self 是什么？ 是一个位置形参
        print(self)
        print('course'+": %s"%name)

    print('类定义完成')

t1  = Teacher('张三',18,'男')
print(t1.__dict__,t1.school,t1.name,t1.age,t1.sex)
# __init__方法传入的属性，对象有，类没有
# 修改属性
t1.name = '李四'
print(t1.name)
t1.course('python')