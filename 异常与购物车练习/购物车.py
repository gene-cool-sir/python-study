# -*-coding:utf-8-*-
'''
购物车：个人信息、字典

'''

# 导入模块
import time

user_idc = {
    'username': 'gene',
    'pwd': '123',
    'locked': False,
    'account': 10000,
    'shopping_cart': {}
}


# 登录
def login():
    '''
    登录函数， 密码输入错误3次锁定5秒用户，用户名输入错误可以一直输入
    :return:
    '''
    print('请登录')
    count = 0
    while True:
        if user_idc['locked']:
            print("你已经输入错误3次，系统锁定5秒， 请等待5秒")
            time.sleep(5)
            user_idc['locked'] = False
            count = 0
        name = input("输入用户名").strip()
        if name == user_idc['username']:
            pwd = input("输入密码").strip()
            if user_idc['pwd'] == pwd and user_idc['locked'] == False:
                print("登录成功")
                break
            else:
                print('密码错误')
                count += 1
        else:
            print("用户名不存在")

        if count > 3:
            user_idc['locked'] = True


#login()

def login_intter(func):
    # shopping
    def wrapper():
        login()
        func()
    return wrapper

# 购物功能
@login_intter  # 装饰器增强， 先登录，再shopping
def shopping():
    print("购物")
    goods_list = [
        ['coffee', 30],
        ['chicken', 20],
        ['iPhone', 8000],
        ['car', 100000],
        ['building', 200000],
    ]

    shopping_cart = {}
    cost_money = 0
    while True:
        print(goods_list)
        # 输入商品对应的编号

        #enumerate 枚举
        for i, item in enumerate(goods_list):
            print(i, item)  # i 是列表的索引； item 是列表的元素

        choice = input("输入商品对应的编号，按t键结账").strip()  # input 输入的是数字吗？ 是字符串数字
        if choice.isdigit():
            # 是字符串数字
            choice = int(choice)
            if choice < 0 or choice > len(goods_list):
                print("请选择相应的序号")
                continue
            # 通过了
            good_name = goods_list[choice][0]
            good_price = goods_list[choice][1]
            # 是否有钱购买
            if user_idc['account'] >= good_price:
                if good_name in shopping_cart:
                    shopping_cart[good_name]['count'] += 1
                else:
                    shopping_cart[good_name] = {'price': good_price, 'count': 1}
                # 金额
                user_idc['account'] -= good_price
                cost_money += good_price
                print("{}新的购物商品".format(good_name))
            else:
                print("钱不够")
        elif choice == 't':
            print(shopping_cart)
            buy = input('买不买（y/n)>>>').strip()
            if buy == 'y':
                if cost_money == 0:
                    print('不买，钱不够')
                    break
                user_idc['shopping_cart'] = shopping_cart
                print('%s 花费了 %s 购买了%s' % (user_idc['username'], cost_money, shopping_cart))
                print('账户信息 %s' % user_idc)
                break
            else:
                print("不买")
                break
        else:
            print("非法输入")


shopping()

# 购物
