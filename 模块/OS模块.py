# -*-coding:utf-8-*-
'''
os 模块
os表示操作系统相关
os与操作系统交互的接口；围绕文件和目录操作
'''

# 工作目录，当前目录，父级目录
import os
# 获取当前目录
print(os.getcwd())
# 获取父级目录
print(os.pardir)
# 获取父级目录
print(os.path.pardir)
# 生成目录
# os.mkdir('test')
# 删除目录
#os.rmdir('test')

#当前脚本的工作目录，相当于cd
#os.chdir('/Python/Python_Learning/python_learning/模块')
# 生成多层递归目录
#os.makedirs('/Python/Python_Learning/python_learning/模块/from模块/test')
# 删除多层递归目录， 存在文件则不行，会有问件保护机制
#os.removedirs('/Python/Python_Learning/python_learning/模块/from模块/test')
# 获取文件列表
print(os.listdir('.'))
# 获取上一级列表
print(os.listdir('..'))
# 重命名文件
#os.rename('test.py', 'test.txt')

# 运行终端命令
os.system('pwd')
# os.path 下的方法 path是路径
# 将path分割成目录和文件
print(os.path.split('..'))
# 返回path 的目录，
print(os.path.dirname('..'))

# 判断路径是否存在（文件或者文件夹都可以）
print(os.path.exists('..'))
# 判断path是否是一个文件
print(os.path.isfile('..'))
# 判断path是否是一个目录
print(os.path.isdir('..'))
# 拼接一个路径，会忽略前面的路径
print(os.path.join('..', '..')) # ..\..


