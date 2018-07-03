from urllib.request import Request,urlopen

import ssl

url = "https://www.12306.cn/mormhweb/"

headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
#创建request对象
request = Request(url,headers=headers)

#请求12306网站的时候，忽略ca认证
context = ssl._create_unverified_context()

#HttpResponse对象
response = urlopen(request,context=context)


#调用HttpResponse的read方法得到数据
html = response.read()
print(html.decode())