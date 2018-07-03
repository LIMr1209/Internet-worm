from urllib.request import Request,build_opener,ProxyHandler


#代理主机账号和主机ip+port
webserver_host = {"http":"trygf521:a4c4avg9@114.67.224.159:16816"}

#代理服务器类
proxy_handler = ProxyHandler(webserver_host)

#自定义opener
opener = build_opener(proxy_handler)

url = "http://www.atguigu.com"

#模拟浏览器请求头信息
head = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
request = Request(url,headers=head)

#HttpRespnse实例对象
response = opener.open(request)

#网页数据
html = response.read()

print(html.decode("utf-8"))





