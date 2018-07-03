from urllib import parse
from urllib.request import Request, urlopen

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
url = 'http://www.baidu.com'

data = {'name': 'zhangsan', 'password': '123456'}

data = parse.urlencode(data).encode()  # post 请求传输需要编码
# 1 post 请求data可以传入 Request
# request = Request(url, headers=headers, data='name=zhangsan&password=123456'.encode())
request = Request(url, headers=headers, data=data)
response = urlopen(request)
# 2 也可以传入Urlopen  都可以
# request = Request(url, headers=headers)
# response = urlopen(request,data=data)


response_data = response.read()

print(response_data.decode())
