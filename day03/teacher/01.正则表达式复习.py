#01.直接是re模块

import re
s = "hello python and aTguigu python!"
ss = re.compile(r"atguigu",re.I)
# result = re.search(r"atguigu",s)

result = ss.search(s)
print(result)

#02.使用re模块compile函数

# import re
# s = "hello python and atguigu python!"
# #正则写在compile
# pattern = re.compile(r"python")
# #开始匹配
# result = pattern.match(s,25,len(s))
# print(result)
# print(result.group())
# print(result.pos)
# print(result.endpos)
# print(result.span())

#03.search 方法的使用,可以指定从那个位置开始搜索

# import re
# s = "hello python and atguigu python!"
# #正则写在compile
# pattern = re.compile(r"python")
# #
# result = pattern.search(s,13,len(s))
# print(result)
# print(result.group())


#04.findall 方法

# s = "one1two2threefour4"
# s = "hello 100,300,xixi,77,88"
#
# import re
# re_so_int = re.compile(r"\d+")
#
# result = re_so_int.findall(s,5,9)
# print(result)



#05. finditer 方法

# s = "one1two2threefour4"
# s = "hello 100,300,xixi,77,88"
#
# import re
# re_so_int = re.compile(r"\d+")
# #返回的是一个迭代对象
# result = re_so_int.finditer(s)
# print(result)
# #for取出内容
# for data in result:
# 	print(data.group())


#06.split的使用
# s = r'a,b;; \ac   d'
#
# #目标:a,b,ac,d
# import re
#
# pattern = re.compile(r"[,;\s\\]+")
#
# result = pattern.split(s)
# print(result)


#07.sub的使用

# s = "hello 123,hello 456"
# #把s对应的内容替换成hello world,hello world
# import re
# pattern = re.compile(r"(\w+) (\w+)")
#
# result = pattern.sub("hello world",s)
# print(result)
#
# def func(m):
# 	# print("m==",m)
# 	# print("m==", m.group(2))
# 	return "hi "+m.group(2)
#
# result = pattern.sub(func,s)
# print(result)
#
#
# #count就是替换的个数
# result = pattern.sub(func,s,1)
# print(result)


#08 匹配中文
# s = "hello world 你好 世界,山丹丹那个花开哟！hehe"
# import re
# pattern = re.compile(r"[\u4e00-\u9fa5]+")
#
# result = pattern.findall(s)
# print(result)

#09.贪婪模式与非贪婪模式
# import re
# pattern = re.compile(r"ab+")
#
# result = pattern.match("abbbbb")
# print(result)
# print(result.group())

# s = "aa<div>;xixi</div>bb<div>test2</div>cc"
# #目标s中获取<div>test1</div>
# import re
# pattern = re.compile(r"<div>.*?</div>")
# result = pattern.search(s)
# print(result)
# print(result.group())








