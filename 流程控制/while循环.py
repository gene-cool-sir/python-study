# while + True 的情况
'''
while True:
    code1
    code2
'''
db_user='gene'
db_pwd='123'
while True:
    input_user = 'gene'
    input_pwd = '123'
    if input_user == db_user and input_pwd == db_pwd:
        print("login successful")
        break;
    else:
        print("login fail")

# while + 条件
start = 0
while start < 9:
    start += 1
    print(start)

print("==================")
# while + continue; continue 代表结束本次循环
start = 0
while start < 9:
    start += 1
    if start == 4:
        continue
    print(start)

print("==================")

# while + break; break 跳出循环
num = 0
while num < 6:
    num += 1
    if num == 5:
       break
    print(num)

# while 遍历列表
names = ['ge','da','he','hei']
i = 0
while i < len(names):
    print(names[i])
    i += 1

