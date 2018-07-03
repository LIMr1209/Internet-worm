from urllib.request import build_opener, HTTPHandler, Request, ProxyHandler

import random

proxy_list = [
	{"http": "122.72.18.35:80"},
	{"36.110.175.130":"8080"},
   {"203.174.112.13":"3128"},

]

# 代理服务器的ip+port
proxy_webserver = random.choice(proxy_list)
print("当前使用的代理服务器是：", proxy_webserver)

# 创建HTTPHanlder
http_handler = ProxyHandler(proxy_webserver)

# 没有设置代理
http_handler_none = ProxyHandler({})

# True使用代理，False不使用代理
proxy_swich = True

if proxy_swich:
	# 自定义opener
	opener = build_opener(http_handler)
else:
	# 没有设置代理，直接请求
	opener = build_opener(http_handler_none)

url = "http://www.atguigu.com"

head = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
# 创建Request实例对象
request = Request(url, headers=head)

# 把Request实例对象传入opener对象里面的open方法
# open方法返回的response是HttpResponse类的实例对象
response = opener.open(request)

# 得到数据
html = response.read()
print("\n", "------------------------")
print(html)
