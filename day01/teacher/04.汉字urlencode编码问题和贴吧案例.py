from urllib import parse
#用户输入要搜索的内容
kw = input("请输入搜索的内容：")
#字典
wd = {"wd":kw}
#url编码
wd = parse.urlencode(wd)
#wd=%E5%B0%9A%E7%A1%85%E8%B0%B7"
print(wd)

print("以上是编码--------------下面就是解码")

#wd=%E5%B0%9A%E7%A1%85%E8%B0%B7"
#wd=%E5%B0%9A%E7%A1%85%E8%B0%B7


# url = "https://www.baidu.com/s?wd=%E5%B0%9A%E7%A1%85%E8%B0%B7"

result = parse.unquote("wd=%E5%B0%9A%E7%A1%85%E8%B0%B7")
print(result)