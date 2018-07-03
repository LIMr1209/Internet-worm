from urllib import parse
from urllib.request import Request,urlopen
#用户输入要搜索的内容
kw = input("请输入搜索的内容：")
#字典
wd = {"wd":kw}
#url编码
wd = parse.urlencode(wd)
print(wd)

#拼接url
url = "https://www.baidu.com/s?"+wd

#请求头信息
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

#构建Request实例对象
request = Request(url,headers=headers)

#返回的实例对象，网络请求
response = urlopen(request)

#返回的数据
content = response.read()

print(content.decode())





