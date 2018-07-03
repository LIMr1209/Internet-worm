from urllib.request import build_opener, ProxyHandler,Request
import random

ip = [
    {'http': '139.129.99.9:3128'},
    {'http': '101.236.19.165:8866'},
    {'http': '101.236.21.22:8866'},
]
ip = random.choice(ip)
proxy_handler = ProxyHandler(ip)
proxy_handler_none = ProxyHandler({})
proxy_switch = True

if proxy_switch:
    opener = build_opener(proxy_handler)
else:
    opener = build_opener(proxy_handler_none)

url = 'https://www.baidu.com'
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
request = Request(url, headers=headers)
response = opener.open(request)

data = response.read()

print(data)
