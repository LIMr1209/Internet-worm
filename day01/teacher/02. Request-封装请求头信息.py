from urllib.request import Request,urlopen

#创建一个Request实例对象，在实例对象里面添加url和请求头，在请求头里面模拟浏览器
url = "http://www.atguigu.com"
# url = "http://192.168.28.85:8080/hello"
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
request = Request(url,headers=headers)

#使用urlopen接收request的实例
response = urlopen(request)

#读取网页数据
data = response.read()
print(data.decode("utf-8"))
