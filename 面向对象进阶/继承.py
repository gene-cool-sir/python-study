# -*-coding:utf-8-*-
'''
继承：
    继承是一个类继承另一个类的一种方式，被继承的类称为父类(Base Class)，继承的类称为子类(Sub Class)。
    python中继承的特点：
        子类可以继承父类的所有属性和方法，也可以定义新的属性和方法。
    子类：
      class Parent(父类）：
            pass
'''

class Parent(object):
    doc = 'parent'
    def __init__(self):
        self.name = 'Parent'
        self.age = 20
        self.sex = 'male'

    def run(self):
        print("我是父类")

class Child(Parent):
    pass

obj = Child()
obj.run()
# 属性查找优先级：子类属性 > 子类方法 > 父类属性 > 父类方法
