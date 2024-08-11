# -*-coding:utf-8-*-
class A:
    print('A')
    pass
class B(A):
    print('B')
    pass
class C(A):
    print('C')
    pass
class D(B):
    print('D')
    pass
class E(C,D):
    print('E')
    pass

obj = D()
obj.x = 111
print(obj.x)
print(E.__mro__) # 输出方法解析顺序
print(E.mro()) # 输出方法解析顺序
print(E.mro()[0].__name__) # 输出方法解析顺序的第一个类名
print(E.mro()[1].__name__) # 输出方法解析顺序的第二个类名
print(E.mro()[2].__name__) # 输出方法解析顺序的第三个类名
print(E.mro()[3].__name__) # 输出方法解析顺序的第四个类名
print(E.mro()[4].__name__) # 输出方法解析顺序的第五个类名
print(E.mro()[5].__name__)# 输出方法解析顺序的第六个类名