# -*-coding:utf-8-*-
'''
hash: 是一种算法， 该算法传授传入的内容，经过运算得到一串hash值
hash特点：
1.只要传入的内容一样，得到的hash值就一样  eg.文件完整性校验
2.不能由hash值反解内容； 把密码做成hash值，不应该在网络中传输明文
3.只要使用hash算法不变，无论检验的内容有多大，得到的hash值长度是固定的，这样不影响传输
'''
import hashlib
# 创建hash工厂
m = hashlib.md5()
# 在内存中创建hash对象，是二进制
m.update('helloworld'.encode('utf-8'))

# 产出hash值
print(m.hexdigest()) #fc5e038d38a57032085441e7fe7010b0

with open('time_test.py', 'rb') as f:
    m.update(f.read())
    print(m.hexdigest())

# 输入密码的时候要用hash算法，把密码变成hash值，再传输，防止被破解
def hash_password(password):
    # 对密码进行hash
    return hashlib.sha256(password.encode('utf-8')).hexdigest()
# 防止撞库，密码前后加盐处理
pwd = '123'
m= hashlib.md5()
# 前后加盐
m.update('before'.encode('utf-8'))
m.update(pwd.encode('utf-8'))
m.update('after'.encode('utf-8'))
print(m.hexdigest())

# hash算法的种类, sha后缀数字越大，加密算法越强，但是加密速度越慢，安全性越高
# md5
# sha1
# sha256
# sha512
m1 = hashlib.sha256()
m1.update('hello world'.encode('utf-8'))
print(m1.hexdigest())

m2 = hashlib.sha512()
m2.update('hello world'.encode('utf-8'))
print(m2.hexdigest())


