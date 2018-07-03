from urllib.request import urlopen, Request, URLError, HTTPError
try:
    request = Request('http://www.baidu.com')
    response = urlopen(request)
except HTTPError as e:
    print('HTTPError:', e)
except URLError as e:
    print('URLError', e)
else:
    print(response.read().decode())
