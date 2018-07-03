from urllib.request import Request, build_opener, HTTPCookieProcessor
from http.cookiejar import CookieJar, MozillaCookieJar

file_name = 'cookie.txt'
# cookie_jar = CookieJar()
# cookie_jar = MozillaCookieJar(filename=file_name)
cookie_jar = MozillaCookieJar()
cookie_jar.load(file_name)
handler = HTTPCookieProcessor(cookiejar=cookie_jar)
opener = build_opener(handler)
request = Request('http://www.baidu.com')
response = opener.open(request)
print(response.read())
cookie_str = ''
for item in cookie_jar:
    cookie_str += item.name + ":" + item.value + ';'
    print(item)
cookie_str = cookie_str[:-1]
print(cookie_str)
# cookie_jar.save()