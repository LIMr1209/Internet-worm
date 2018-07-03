from urllib.request import Request, urlopen
import ssl

context = ssl._create_unverified_context()

url = 'https://www.12306.cn/mormhweb/'
headers = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}
request = Request(url, headers=headers)

response = urlopen(request, context=context)

content = response.read()
print(content.decode())
