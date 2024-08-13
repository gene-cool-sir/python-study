# -*-coding:utf-8-*-
'''
序列化和反序列化
序列化是把一个对象变成可存储或传输的过程
反序列化是把可存储或传输的对象变成对象的过程
# 常用方法
序列化：
dump : 处理文件
dumps : 处理字符串
反序列化
load : 处理文件
loads: 处理字符串
'''
# 数据可跨平台交互
import json

data = {
    'name': 'Bob',
    'age': 20,
    'score': 88
}
json_str = json.dumps(data)
print(json_str)
print(type(json_str))
# 把json_str 写入文件, dump(数据类型，文件对象)
with open('data.json', 'w') as f:
    json.dump(json_str, f)

# 反序列化
with open('data.json', 'r') as f:
    data = f.read()
    print(data)
    # json.loads(字符串) 转对象, 反序列化
    dic = json.loads(json_str)
    print(dic)



