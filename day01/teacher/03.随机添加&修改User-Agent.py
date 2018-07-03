from urllib.request import Request,urlopen
import random

#创建一个Request实例对象，在实例对象里面添加url和请求头，在请求头里面模拟浏览器
# url = "http://www.atguigu.com"
# url = "http://192.168.28.85:8080/hello"
url = "https://www.baidu.com/s?wd=尚硅谷"
url = "https://www.baidu.com/s?wd=%E5%B0%9A%E7%A1%85%E8%B0%B7"
headers = [
"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0",
"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/7.0)"
]

# headers = random.choice(headers)
#
# headers = {"User-Agent":headers}#字典

# request = Request(url,headers=headers)
request = Request(url)

headers = random.choice(headers)
request.add_header("user-agent",headers)



#使用urlopen接收request的实例
response = urlopen(request)

#读取网页数据
data = response.read()
print(data.decode("utf-8"))

#获取添加的信息,很大坑
print(request.get_header("User-agent"))

print(response.geturl())
print(response.info())
