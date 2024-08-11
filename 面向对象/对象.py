# -*-coding:utf-8-*-
'''
对象的使用：
    1. 类的实例化， 调用类的返回值称之为类的一个对象(实例）

'''


class Teacher:
    # 属性、特征
    name = '张三'
    age = 18
    sex = '男'

    # 函数
    def course(self):
        print('上课')
        # self 是什么？ 是一个位置形参
        print(self)
        print('course')

    print('类定义完成')


# 创建对象
teacher = Teacher()
t2 = Teacher()
print(teacher.name, teacher)
print(t2.name, t2)

# 这些对象没有独立的属性， 用的是类的属性和方法
print(teacher.__dict__)
print(teacher.course())  # 通过对象调用的函数不需要传递self参数， self参数是指对象本身; 对比类执行方法必须传递参数

# 对象属性的修改，初始属性来自类，本身无属性
teacher.name = '李四'
print(teacher.name, t2.name, Teacher.name)
# 对象添加属性，本身有属性，类无属性
teacher.address = '北京'
print(teacher.address)
# 删除对象属性
del teacher.address  # 对象删除属性
del teacher.name  # 对象删除类属性，类属性不变
print(teacher.name)
