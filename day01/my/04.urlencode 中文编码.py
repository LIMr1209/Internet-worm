from urllib import parse
from urllib.request import Request, urlopen

kw = input('输入搜索的内容')

wd = {'wd': kw}
# url 编码
wd = parse.urlencode(wd)

print(wd)
# url 解码
a = parse.unquote(wd)

print(a)
# get 请求
url = 'http://www.baidu.com/s?' + wd

header = {
    "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
}

request = Request(url, headers=header)

response = urlopen(request)

data = response.read()

print(data.decode())
