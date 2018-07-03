from urllib.request import ProxyHandler, Request, build_opener
import random
ip = [
    '101.236.60.52:8866',
    '114.212.12.4:3128',
    '118.190.95.35:9001'
]

ip = random.choice(ip)

# httpproxy_handler = ProxyHandler({'http':'用户名:密码@ip:端口'})

httpproxy_handler = ProxyHandler({"http": ip})
nullproxy_handler = ProxyHandler()
proxySwitch = True
if proxySwitch:
    opener = build_opener(httpproxy_handler)
else:
    opener = build_opener(nullproxy_handler)
url = 'http://www.baidu.com'
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
request = Request(url, headers=headers)
response = opener.open(request)

data = response.read()

print(data.decode())
print(ip)