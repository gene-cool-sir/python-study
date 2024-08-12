# -*-coding:utf-8-*-
'''
隔离复杂度： 不需要使用者直到方法
'''

class ATM:
    def __card(self):
        print('请输入卡号')
    def __auth(self):
        print('请输入密码')

    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__take_money()

a = ATM()
a.withdraw()
