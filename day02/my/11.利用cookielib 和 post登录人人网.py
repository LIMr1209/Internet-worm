from urllib.request import Request, build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar
from urllib import parse

cookie_jar = CookieJar()
handler = HTTPCookieProcessor(cookiejar=cookie_jar)
opener = build_opener(handler)

url = 'http://www.renren.com/PLogin.do'
data = {'email': "aaa1058169464@126.com", 'password': 'aaa1058169464'}
data = parse.urlencode(data).encode()
request = Request(url, data=data)
request.add_header('User-Agent',
                   'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36')
response = opener.open(request)
print(response.read().decode())
