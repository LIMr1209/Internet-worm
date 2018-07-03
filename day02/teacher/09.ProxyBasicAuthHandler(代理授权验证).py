from urllib.request import Request,build_opener,ProxyHandler,ProxyBasicAuthHandler,HTTPPasswordMgrWithDefaultRealm

#管理账号和密码
http_password_mgr = HTTPPasswordMgrWithDefaultRealm()
#代理主机账号和主机ip+port
# webserver_host_port = {"http":"trygf521:a4c4avg9@114.67.224.159:16816"}

#代理服务器ip+端口
webserver_host_port = "114.67.224.159:16816"

#用户
user = "trygf521"
#密码
password = "a4c4avg9"

#第一个参数：None

http_password_mgr.add_password(None,webserver_host_port,user,password)

#代理服务器类
proxy_handler = ProxyBasicAuthHandler(http_password_mgr)

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





