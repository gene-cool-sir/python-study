# -*-coding:utf-8-*-
# 总结对象的相似之处得到了类
# 总结类的相似之处得到父类

class Person(object):
    school = "四川大学"

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    #def __init__(self,name,age):
    #    self.name = name
    #   self.age = age
    def play(self):
        print("%s正在玩" % self.name)


class Teacher(Person):
    #def __init__(self, name, age):
    # self.name = name
    # self.age = age

    def __init__(self, name, age, money):
        Person.__init__(self, name, age)  # 调用父类的__init__方法进行初始化属性，此方式并没有使用继承，而是直接调用父类的方法
        self.money = money

    def teach(self):
        print("%s正在教" % self.name)


s1 = Student("张三", 18)
print(s1.__dict__)
t1 = Teacher("李四", 20, 10000)
print(t1.__dict__)
# 子类和父类都有__init__方法，子类会覆盖父类的__init__方法
# 子类需要有自己特有的属性，方式一： 在子类的__init__方法中调用父类的__init__方法
t1.teach()




