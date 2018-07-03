from urllib.request import build_opener,HTTPHandler,Request, HTTPSHandler

#创建HTTPHanlder
http_handler = HTTPHandler(debuglevel=1)

#自定义opener
opener = build_opener(http_handler)
url = "http://www.atguigu.com"

head = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
#创建Request实例对象
request = Request(url,headers=head)

#把Request实例对象传入opener对象里面的open方法
#open方法返回的response是HttpResponse类的实例对象
response = opener.open(request)


#得到数据
html = response.read()
print("\n","------------------------")
print(html)