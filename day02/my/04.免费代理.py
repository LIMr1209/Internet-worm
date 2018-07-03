from urllib.request import Request,ProxyHandler,build_opener

proxy_handler = ProxyHandler({'http':'61.135.217.7:80'})
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
request = Request(url,headers=headers)
response = opener.open(request)

data = response.read()

print(data)