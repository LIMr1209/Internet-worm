from urllib.request import Request, urlopen
from urllib import parse

url = 'http://httpbin.org/post'

data = {"name": "zhangsan", "age": "18"}

data = parse.urlencode(data).encode()

headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}

request = Request(url, headers=headers)

response = urlopen(request, data=data)

content = response.read()

print(content.decode())
