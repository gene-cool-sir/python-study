# -*-coding:utf-8-*-
import random
# 0 -1 随机浮点， 不包含1 random 0-1 开闭
print(random.random())
# randint 1-3
print(random.randint(1, 3))
# 0-2 随机整数， 1-3 开闭
print(random.randrange(0, 3))
# 随机选一个
print(random.choice([1, 2, 3, 4, 5]))

# 随机指定个数
print(random.sample([1, 2, 3, 4, 5], 3))
# 打乱顺序
print(random.shuffle([1, 2, 3, 4, 5]))
# 闭闭 浮点
print(random.uniform(1, 3))

