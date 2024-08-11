# -*-coding:utf-8-*-
'''
什么是组合
 组合是某一个对象拥有一个属性，该属性的值是另外一个类的对象

'''


class Foo:
    xx = 100


class Bar:
    yyy = 200

    def zzz(self):
        print("i am bar object")


obj = Foo()
obj1 = Bar()
print(obj.xx)
print(obj1.yyy)

obj.attr = obj1
# obj.attr 等价于 obj1
print(obj.attr.yyy)

obj.attr1 = obj1
print(id(obj.attr), id(obj.attr1))

'''
 通过某一个对象的属性是另一个对象，来完成属性查找， 减少代码冗余
'''


class Person(object):
    school = "四川大学"

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name, age, sex):
        super().__init__(name, age)  # 调用父类的__init__方法进行初始化属性，此方式并没有使用继承，而是直接调用父类的方法
        self.sex = sex

    def play(self):
        print("%s正在玩" % self.name)


class Teacher(Person):
    def __init__(self, name, age, money):
        # Person.__init__(self, name, age)  # 调用父类的__init__方法进行初始化属性，此方式并没有使用继承，而是直接调用父类的方法
        Person.__init__(self, name, age )  # 子类继承父类，使用super()方法，super()方法会去查找父类，然后调用父类的方法，

        self.money = money

    def teach(self):
        print("%s正在教" % self.name)


class Course(object):

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def tell_info(self):
        print("课程名称：%s,课程价格：%s" % (self.name, self.price))


python = Course("python", 100)
math = Course("math", 200)
english = Course("english", 300)

teacher = Teacher("张三", 20, 20000)
# 把english课程添加到teacher的课程列表中
teacher.course_list = [python, math, english]
teacher.course_list[0].tell_info()
teacher.course_list[1].tell_info()
