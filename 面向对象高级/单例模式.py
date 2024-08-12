# -*-coding:utf-8-*-
# 绑定类方法的单例模式
class Singleton(object):
    __instance = None

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port

    @classmethod
    def from_conf(cls):
        print("绑定类方法")
        if cls.__instance is None:
            cls.__instance = cls("127.0.0.1", 8080)  # 完成初始化
        return cls.__instance


# 调用绑定类方法，这样是单例，多次得到的对象指向同一个对象
obj = Singleton.from_conf()
obj1 = Singleton.from_conf()
print(obj,
      obj1)  # 输出：<__main__.Singleton object at 0x0000020B0B0C0F60> <__main__.Singleton object at 0x0000020B0B0C0F60>

# 调用类实例, 这样不是单例
p = Singleton("127.0.0.1", 8080)
p1 = Singleton("127.0.0.1", 8081)
