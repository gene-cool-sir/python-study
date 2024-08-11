# -*-coding:utf-8-*-

class Foo():
    name = 'Foo'
    def f1(self):
        print('f1')
    def f2(self):
        print('f2')

class Barl(Foo):
    name = 'Barl'
    def f1(self):
        print('barl.f1')

class Bar(Barl):
    name = 'Bar'
    def f1(self):
        print('bar.f1')

obj = Bar()
obj.name = 'obj'
print(obj.name)
print(Bar.mro())
print(obj.f2()) # 找不到，所以会去父类找


