# -*-coding:utf-8-*-
"""
__str__
__del__
__call__

"""
# __str__ 在对象被打印的时候自动触发，可以返回一个字符串
class Person(object):
    school = "四川大学"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return "name: %s, age: %s" % (self.name, self.age)

person = Person("张三", 18)
print(person)

# __del__ 在对象被删除的时候自动触发该方法， 可以用来回收对象意外的其他相关资源， 比如系统资源
class SD(object):
    school = "四川大学"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __del__(self):
        print("对象被删除了")
sd = SD("张三", 18)
del sd

#__call__ : 在对象被调用时自动触发该方法
class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __call__(self, *args, **kwargs):
        print("name: %s, age: %s" % (self.name, self.age))
foo = Foo("张三", 18)
# 在类里面没有__call__方法，直接调用foo()会报错，但是如果foo()有__call__方法，那么foo()就相当于调用了foo.__call__()方法
foo() # 自动调用__call__方法
