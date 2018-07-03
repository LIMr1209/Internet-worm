from urllib.request import Request, urlopen, URLError, HTTPError

url = 'http://www.baidu.com'
headers = {
    "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/67.0.3396.99 safari/537.36",
}
try:
    request = Request(url, headers=headers)

    response = urlopen(request)
except HTTPError as e:
    print('HTTPError:', e)
except URLError as e:
    print('URLError:', e)
else:
    print(response.read().decode())
