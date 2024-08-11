# -*-coding:utf-8-*-
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
        #Person.__init__(self, name, age)  # 调用父类的__init__方法进行初始化属性，此方式并没有使用继承，而是直接调用父类的方法
        #super(Person,self).__init__(name,age) # 子类继承父类，使用super()方法，super()方法会去查找父类，然后调用父类的方法，
        super().__init__(name,age) # super()方法会去查找父类，然后调用父类的方法，
        self.money = money

    def teach(self):
        print("%s正在教" % self.name)

'''
 # supper(自己的类名，自己的对象）
 # supper() # 可以省略
'''
teacher = Teacher("张三", 30, 1000)
teacher.teach()