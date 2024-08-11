# -*-coding:utf-8-*-
class Teacher:
    # 属性、特征
    school = '成都川大' # 类中的属性，所有对象都有
    def __init__(self,name,age,sex): # self 会自动传递， 其余为形参属性
        print('初始化')
        self.name = name
        self.age = age
        self.sex = sex

    # 函数
    def course(self,name):
        print('上课')
        # self 是什么？ 是一个位置形参
        print(self)
        print('course'+": %s"%name)

    print('类定义完成')

t1 = Teacher('张三',18,'男')
t2 = Teacher('李四',20,'女')
t3 = Teacher('王五',22,'男')
# 对象属性查找, 类的属性给对象使用， 是共享的
print(id(t1.school))
print(id(t2.school))
print(id(Teacher.school))

# 类属性变化, 对象有自己的属性会优先使用自己的属性
Teacher.pypy = '哈哈'
t1.pypy = '哈哈t1'
print(t1.pypy,Teacher.pypy,id(t1.pypy),id(Teacher.pypy))

# 对象调用类的方法，不需要传入参数self; 类调用需要传入参数self(对象的self代表实例，类的self代表一个形参）
# 类调用方法必须传入形参，对象调用方法不需要传入形参self



