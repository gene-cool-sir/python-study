# -*-coding:utf-8-*-
'''
 property 是一种特殊的属性，访问它会执行一段功能（函数），然后返回值

'''
class Person(object):
    def __init__(self, name, weight, height, age):
        self.name = name
        self.weight = weight
        self.height = height
        self.age = age

    @property # 把一个方法变成属性调用,
    def bmi(self):
        return self.weight / (self.height**2)

p = Person('张三', 80, 1.7, 20)
# print(p.bmi()) # 不适用@property的话，需要这样调用
print(p.bmi) # 使用@property的话，可以直接调用属性
