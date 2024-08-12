# -*-coding:utf-8-*-
'''
Python 中统一了类和类型
元类： 对象都是由类创建得到

'''
class Teacher(object):
    def __init__(self, name):
        self.name = name
    def teach(self):
        print('%s is teaching' % self.name)

t = Teacher('Bob')
print(type(t))
print(type(Teacher)) # Teacher 属于 type这个类

# 对象t 是Teacher类的一个实例; Teacher 是 type 类的一个实例; 都是调用一个类实例化得到的 Teacher=元类（...）内置的元类type
# 调用元类获取到一个自定义的类； 调用自定义的类创建一个自定义的对象
print(isinstance(t, Teacher))


'''
 type元类创建自定义类
 自定义类： 类名、类的基类object、类命名空间
 
 class 关键字创建自定义类的底层原理：
 1. 先拿到类名
 2. 再获取基类（object,)
 3. 再获取命名空间（执行类体代码，将产生的名字放到类的名称空间也就是一个字典__dict__)
 4.调用元类type创建类： Teacher = type(类名，基类，命名空间,代码体)
'''

# 不依赖class 关键字创建一个自定义类
class_name = 'Students'
base_class = (object,)
class_body = '''
HP=100
def __init__(self, name):
    self.name = name
def run(self):
    print('running')
'''
class_dic={}
# exec 函数： exec(code, globals, locals)
exec(class_body, {}, class_dic)
Students =type(class_name,base_class,class_dic)
s = Students('Bob')
print(s.name)


# 自定义元类
# 自定义元类， 然后创建自定义类
class Mymeta(type):
    # 但凡继承了type的都是一个自定义元类，否则是一个普通的类
    def __init__(cls, name, bases, attrs):
        print('__init__')
        print(name, bases, attrs)
        if class_name.islower():
            raise TypeError('类名必须大写')
        print(attrs.get('__doc__'))
        if attrs.get('__doc__') is None:
            raise TypeError('类必须写注释')
    def __new__(cls, name, bases, attrs):
        print('__new__')
        return type.__new__(cls, name, bases, attrs)

    def __call__(self, *args, **kwargs):
        print('meta-call')
        newobj = self.__new__(self) # __new__创建一个空对象
        self.__init__(newobj, *args, **kwargs)

        k1,v1=[],[]
        for k,v in newobj.__dict__.items():
            print(k,v,self.__name__)
            print('形成影藏属性的写法----')
            print('_%s__%s'%(self.__name__,k))
            k1.append('_%s__%s'%(self.__name__,k))
            v1.append(v)

        newobj.__dict__ = dict(zip(k1,v1))


        return newobj
class Math(object, metaclass=Mymeta):
    '''
    我是注释，可以被__doc__识别
    '''
    HP='dada'
    def __init__(self, name):
        self.name = name

    def __call__(self, *args, **kwargs):
        print('call')

math = Math('Bob')
print(math)

# 自定义元类控制类的产生
math()
print(math.__dict__)

# 列表生成式
print([i*i for i in range(0,10)])
# 只拿偶数， 可以使用if
print([i*i for i in range(10) if i%2==0])




