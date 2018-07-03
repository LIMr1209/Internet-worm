from urllib.request import Request,urlopen

#创建Request对象，配置url和headers
url = "http://www.baidu.com"
url = "http://192.168.28.123:8080"

headers = {
"User-Agent": " Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0"
}

#在Request传入data也是post请求
request = Request(url,headers=headers,data="name=afu&password=afu123456".encode("utf-8"))


#把Rquest传入urlopen，请求并且返回对象
#data传入数据就是post请求
reponse = urlopen(request)

#根据返回的对象，调用read方法，得到数据
data = reponse.read()#bytes
print(data)

