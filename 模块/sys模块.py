# -*-coding:utf-8-*-
# sys模块是Python解释器交互的一个接口

import sys
# sys.path 模块搜索路径, 初始化时使用PYTHONPATH环境变量的值
print(sys.path)

# from 的目录， 默认是当前目录， 如果模块名不是当前目录，则从sys.path中搜索
# sys.path.insert(0, '') 或者 sys.path.append('') 把模块搜索路径添加到列表的最前面或者最后面， 然后就可以使用 from模块 import 模块名
