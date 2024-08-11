# -*-coding:utf-8-*-
'''
面向过程：
    它强调的是通过一系列的过程调用（即函数调用来实现特定的功能）来构建程序。这种编程方法通常不涉及数据封装和抽象，而是更侧重于将复杂的任务分解为一系列简单的步骤或过程。

面向对象：
    类、类属性、类方法、实例、实例属性、实例方法
    类：对象是什么？是一些列对象相同的特征和行为的集合
    对象：具体存在的失误，类是一个抽象概念
'''

# 类的使用
'''
类语法：
    class 定义类的关键字 # 首字母大写
    
class 类名：
    pass
#驼峰体
class Person:
    pass
    
'''
# 定义类
class Teacher:
    # 属性、特征
    name = '张三'
    age = 18
    sex = '男'
    # 函数
    def course(self):
        print('上课')
        # self 是什么？ 是一个位置形参
        print('course')
    print('类定义完成')

# 类是一系列对象的相同属性和行为的结合体；类体中最常见的就是变量和函数的定义
print(Teacher.__dict__)

# 调用类的属性
print(Teacher.name,Teacher.age,Teacher.sex)
# 调用类的方法
print(Teacher.course(11))

# 修改属性的值
Teacher.name = '李四'
print(Teacher.name)
# 添加类的属性
Teacher.address = '北京'
print(Teacher.address)
# 删除类的属性
del Teacher.address
print(Teacher.__dict__)

'''
1. 类的本质是一个用来存放变量和函数的容器
2. 类而用途： 1. 当作容器从内部取出来名字使用
3. 调用类来产生对象
'''
