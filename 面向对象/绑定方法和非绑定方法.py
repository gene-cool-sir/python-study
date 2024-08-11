# -*-coding:utf-8-*-
'''
类和对象方法的绑定
self 绑定给定对象方法： 对象调用的时候会把自己作为参数传入；这个参数我们用self表示

'''


class A:
    def f(self):
        print(self)


a = A()
print(a.f(), a)
print(A.f(a), a)


# 是哪个对象调用的self参数的方法， 那么传入的self就是哪个对象

# 绑定给类的方法
class B:
    @classmethod
    def f(cls):
        print(cls)


# 添加@classmethod之后，cls参数就表示类本身了
print(B, B.f(), B().f())


# 非法绑定方法、静态方法
class C:
    # 大部分方法都是对象的方法，可能就没有设计 @selfmethod 这种注解
    def f(self): # 绑定给定对象方法： 对象调用的时候会把自己作为参数传入；这个参数我们用self表示
        print(self)

    @staticmethod  # 非静态方法，不会自动传入对象或者类
    def g():
        print('static')

    @classmethod
    def h(cls): # 静态方法，传入的是类本身
        print('class')

c = C()
print(C.f(c), C.g(), C.h())

'''
绑定方法：绑定给谁就由谁来调用，调用就会将自己作为第一个参数自动传入
    绑定方法分为2类：
    1. 绑定给对象的方法： 在类内部定义的函数，在类外部创建的对象调用的时候会自动传入self参数
    2. 绑定给类调用的方法： 在类内部定义的函数，如果@classmethod装饰，那么是绑定给类的，应该由类调用，类来调用自动将类cls作为第一个参数自动传入
3. self cls 无需外部类 （ @staticmethod @classmethod)
'''