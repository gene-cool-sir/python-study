# --coding:utf-8--

# 字符串操作
msg = 'hello world'
print(msg[0])
print(msg[-1])
# 2. 切片，查找字符串当中的一段只【起始值:终止值：步长] 是一个左包右开
print(msg[0:3:1])
# 提取值，并不会改变原值
print(msg[::])
# 反向取，步长是负数
print(msg[::-1])
# 3. 长度方法 可以计算长度
print(len(msg))
# 4. 布尔类型True,False
print('dabai' in msg)
print('haha' not in msg)
# 5. 字符串拼接
print('haha' + "haode")
# 6. format
print('my name is {}'.format("gene"))
print('my name is {1} my age is {0}'.format(18, 'gene'))
print('my name is {name} my age is {age}'.format(age=19, name='gene'))
# 7. join
str1="好人"
str2="nishi"
str3="你是一个好人"
print(''.join([str1,str2,str3]))
print('，'.join([str1,str2,str3]))
# 空格也属于字符串
# 8.删除字符串
name='gene'
del name
# 9.改字符串
#字符串大小写修改，原值是不会变的，需要新变量接收; 他是一个不可变类型
updatemsg = 'abc'
updatemsg1 = updatemsg.upper();
print(id(updatemsg1),id(updatemsg), updatemsg1)
# 把第一个字母转换为大写 capitalize
print(msg.capitalize())
# 把每个单词的首字母转大写 title
print(msg.title())
# 把字符串切分为列表， split 默认是以空格为切分
print(msg.split())
split_msg = "hello*world*python"
print(split_msg.split("*"))
print(split_msg.split("*")[0])
# 去掉字符串左右2边的字符strip 不写默认是空格字符，不管中间的其他字符
strip_msg=" da hai "
print(strip_msg.strip())
# 了解 center, ljust, rjust
print("dahai".center(11,"*"))
print("dahai".ljust(11,"*"))
print("dahai".rjust(11,"*"))
# 10.查找字符串
find_msg='hello dahai is dsb'
print(find_msg.find("dahai")) # 查找子字符串在大字符串中的位置（首字母）
print(find_msg.find("ddd")) # 没找到返回-1
# pring(find_msg.index("ddd")) # 没找到会报错
print(find_msg.count("dahai")) # 统计一个字符串在大字符串出现的次数
# 判断一个字符串的数据是不是都是数字 isdigit 返回布尔值
digit_msg='1818'
print(digit_msg.isdigit())
# 判断每个元素是不是都是字母 isalpha
alpha_msg='hello'
print(alpha_msg.isalpha())
# 以什么开头和结尾 startswith endswith
print(alpha_msg.startswith("h"))
print(alpha_msg.endswith("o"))
# 判断字符串中的值是否都是大写或者小写 isupper islower
upper_msg="AND"
print(upper_msg.isupper())
print(upper_msg.islower())
# 11.字符串的转义 加了 \ 字符不再表示它本身的含义 常用的 \n \t
print('hello \n world')
print(r'hello \n haha') # 添加r取消字符串中的所有转义
print('hello \\n haha') # 使用双转






