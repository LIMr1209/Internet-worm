from urllib.request import Request, urlopen, build_opener, HTTPCookieProcessor
from http.cookiejar import MozillaCookieJar

filename = "baidu_cookie.txt"
cookiejar = MozillaCookieJar()

cookiejar.load(filename=filename)
# 用户http出来cookie的类
handlers = HTTPCookieProcessor(cookiejar=cookiejar)

# 自定义opener
opener = build_opener(handlers)

url = "http://www.baidu.com"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
}
request = Request(url, headers=headers)

http_response = opener.open(request)

data = http_response.read()

print(data.decode())


#取出cooke
print(cookiejar)
cook_str = ""
for cook in cookiejar:
	# print(cook)
	cook_str = cook_str+cook.name+"="+cook.value+";"


print(cook_str[:-1])

# cookiejar.save()



