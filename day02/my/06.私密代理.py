from urllib.request import Request, ProxyHandler, build_opener

host_server = {'http': 'trygf521:a4c4avg9@114.67.224.159:16816'}  # '用户名:密码@ip:端口'
http_handler = ProxyHandler(host_server)
http_handler_none = ProxyHandler({})
proxySwitch = True
if proxySwitch:
    opener = build_opener(http_handler)
else:
    opener = build_opener(http_handler_none)

url = 'http://www.atguigu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
request = Request(url, headers=headers)
response = opener.open(request)
data = response.read()
print(data)
