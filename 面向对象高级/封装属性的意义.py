# -*-coding:utf-8-*-
'''
封装属性： 将数据的属性进行隐藏，类外无法直接操作属性，只能间接使用
需要类开辟一个接口来对外进行使用操作属性
更加严格的控制属性的操作

'''

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    def tell_info(self):
        print('姓名：%s,年龄：%d'%(self.__name,self.__age))
        print(self.__dict__)
    def set_info(self,name,age):
        if type(name) is not str:
            print('姓名必须为字符串')
            return
        if type(age) is not int:
            print('年龄必须为整数')
            return
        self.__name = name
        self.__age = age
        print(self.__dict__)
        print('姓名：%s,年龄：%d'%(self.__name,self.__age))

obj = Person('张三',20)
obj.tell_info()
obj.set_info('李四',30)

