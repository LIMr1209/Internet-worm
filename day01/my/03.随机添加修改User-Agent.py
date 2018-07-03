from urllib.request import Request, urlopen
import random

url = 'http://www.baidu.com'
header = [
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;'
]

header = random.choice(header)

request = Request(url)
request.add_header('User-Agent', header)

response = urlopen(request)

data = response.read()

print(data.decode())
print(request.get_full_url())
print(request.get_header('User-agent'))
print(response.getcode())
print(response.geturl())
print(response.info())