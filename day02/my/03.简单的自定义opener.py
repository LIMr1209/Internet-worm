from urllib.request import Request,urlopen,build_opener,HTTPHandler,HTTPSHandler

handler = HTTPHandler(debuglevel=1)
# handler = HTTPSHandler(debuglevel=1)
opener = build_opener(handler)

url ='http://www.baidu.com'

request = Request(url)

response = opener.open(request)

data = response.read()

print(data)