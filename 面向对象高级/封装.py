# -*-coding:utf-8-*-
'''
封装：
封装属性、封装函数；在类内定义的属性前加__开头
__ 开头的属性或者方法会被隐形的变形为： _类名__属性名; 在类定义的阶段，会自动将属性名前加_类名
'''
class Person:
    x = 1
    __y = 2 # 私有属性, 类不能直接调用 需使用get/set方法
    def __init__(self,name,age):
        self.name = name
        self.__age = age
    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age
print(Person.__dict__)
print(Person._Person__y) # 类外调用私有属性, 这样并不会整的限制类外访问, 此操作只会在类定义阶段检测语法时发生一次
Person.__z = 123
print(Person.__z) # 这个是类外新增的属性，这样并不会整的限制类外访问
print(Person('haha',20).get_age())

class Foo:
    def __f1(self):
        print('foo.f1')

    def f2(self):
        print('foo.f2')
        self.__f1() # _Foo__f1(self) 等同 self._Foo__f1()

class Bar(Foo):
    def __f1(self):  # 等同 _Foo__f1(self)
        print('bar.f1')

bar = Bar()
print(Bar.__dict__)
bar.f2()  # 等同于调用Foo.f2(bar) , 然后内部调用的是_Foo__f1(bar);