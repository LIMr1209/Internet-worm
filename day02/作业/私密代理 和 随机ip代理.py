from urllib.request import Request, ProxyHandler,build_opener
import random
# server_ip =[
#     {'http': '139.129.99.9:3128'},
#     {'http': '101.236.19.165:8866'},
#     {'http': '101.236.21.22:8866'},
# ]
# server_ip = random.choice(server_ip)
server_ip = {'http':'trygf521:a4c4avg9@114.67.224.159:16816'}
proxy_handler = ProxyHandler(server_ip)
proxy_handler_none = ProxyHandler({})
proxySwitch = True
if proxySwitch:
    opener = build_opener(proxy_handler)
else:
    opener = build_opener(proxy_handler_none)
url = 'https://www.baidu.com'
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
request = Request(url,headers=headers)
response = opener.open(request)
print(response.read().decode())
