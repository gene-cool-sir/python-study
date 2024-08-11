# -*-coding:utf-8-*-
'''
多态： 同一种事物有多种形态，多种形态具有相同的特征，但具有不同的功能。

'''
class Animal(object):
    def speak(self):
        print("Animal speak")
class Dog(Animal):
    def speak(self):
        print("Dog speak")
class Pig(Animal):
    def speak(self):
        print("Pig speak")

# 多态性
animal = Animal()
dog = Dog()
pig = Pig()
animal.speak()
dog.speak()
pig.speak()

# 内置方法多态
print(len("abc"))

