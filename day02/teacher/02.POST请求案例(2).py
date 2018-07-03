from urllib.request import Request,urlopen
from urllib import parse

#创建Request对象，配置url和headers
url = "http://www.baidu.com"
url = "http://192.168.28.123:8080"

data = {"name":"afu","password":"afu123456"}

#name=afu&password=afu123456

data = parse.urlencode(data).encode()

headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

#在Request传入data也是post请求
request = Request(url,headers=headers)
from http.client import HTTPResponse

#把Rquest传入urlopen，请求并且返回对象(HttpResponse)
#data传入数据就是post请求
reponse = urlopen(request,data=data)

#根据返回的对象，调用read方法，得到数据
data = reponse.read()#bytes
print(data.decode())
print(type(data))

