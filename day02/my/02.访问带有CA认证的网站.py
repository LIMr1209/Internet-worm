from urllib.request import Request, urlopen
import ssl
import random

# 忽略CA认证
context = ssl._create_unverified_context()

url = "https://www.12306.cn/mormhweb/"

headers = [
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
]

request = Request(url)
headers = random.choice(headers)
request.add_header('User-Agent', headers)

response = urlopen(request, context=context)

content = response.read()

print(content.decode())
