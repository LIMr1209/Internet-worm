from urllib.request import Request, build_opener, ProxyHandler
import random

server_host = [
    {'http': '139.129.99.9:3128'},
    {'http': '101.236.19.165:8866'},
    {'http': '101.236.21.22:8866'},
]

server_host = random.choice(server_host)
# server_host = {'http':'trygf521:a4c4avg9@114.67.224.159:16816'}
handler = ProxyHandler(server_host)
handler_none = ProxyHandler({})
proxySwitch = True
if proxySwitch:
    opener = build_opener(handler)
else:
    opener = build_opener(handler_none)
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
request = Request('http://www.baidu.com', headers=headers)
response = opener.open(request)

print(response.read())
