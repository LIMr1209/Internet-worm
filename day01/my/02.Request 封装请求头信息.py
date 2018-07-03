from urllib.request import Request, urlopen

url = 'http://www.baidu.com'
header = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
request = Request(url, headers=header)

response = urlopen(request)

data = response.read()
print(data.decode())
