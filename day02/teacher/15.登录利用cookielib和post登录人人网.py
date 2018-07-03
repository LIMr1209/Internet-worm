from urllib.request import build_opener,HTTPCookieProcessor,Request
from http.cookiejar import CookieJar
from urllib import parse

#动态装cookie,在内存中
cookiejar = CookieJar()
#出来cookie处理器
handler = HTTPCookieProcessor(cookiejar=cookiejar)

opner = build_opener(handler)

#添加头信息
opner.addheaders = [('User-agent', "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36")]

url = "http://www.renren.com/PLogin.do"

data = {
	"email":"yangguangfu2017@163.com",
	"password":"afu123456"

}

#转换成email=yangguangfu2017@163.com&password=afu123456
data = parse.urlencode(data).encode()
print(data)

reqeust = Request(url,data=data)

response = opner.open(reqeust)

html = response.read()
print(html.decode())