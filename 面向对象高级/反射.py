# -*-coding:utf-8-*-
'''
 反射： 通过字符串来反射到对象或者类的属性上

'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print('%s is runninng'%self.name)

p = Person('张三',20)
print(p.name)
print(p.__dict__)
p.name="lisi"
p.sex="男"
print(p.__dict__)
del p.sex
print(p.__dict__)

# 让用户使用属性
# p.'name' # 用户输入一个字符串，通过反射得到属性
print(hasattr(p,'name')) # 判断属性是否存在
# 获取对象的属性
print(getattr(p,'name'))
print(getattr(p,'name1', None))

# 修改属性
setattr(p,'name','wangwu')
print(p.name)
# 修改不存在的属性，直接添加
setattr(p,'sex','男')
print(p.__dict__)

# 删除对象属性
delattr(p,'sex')
print(p.__dict__)

# 类也可以使用反射 hasattr(类， 属性或者方法)
print(hasattr(Person,'run'))

# 反射方法的应用
class ShoppingCart:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        self.items.append(item)
    def remove_item(self,item):
        self.items.remove(item)
    def get_total_price(self):
        total = 0
        for item in self.items:
            total += item.price
        return total
    def print_items(self):
        for item in self.items:
            print(item.name,item.price)

    def checkout(self):
        if hasattr(self, 'get_total_price'):
            total = self.get_total_price()
            print('Total price:', total)
        else:
            print('No total price method')

shop = ShoppingCart()
shop.checkout()


# 可以通过判断是否有哪个方法， 然后反射hasattr 判断是否有这个方法， 然后执行相应的代码逻辑


