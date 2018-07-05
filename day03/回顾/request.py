import requests

# kw = {'wd': '尚硅谷'}
# headers = {
#     "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
# }
# response = requests.get('http://www.baidu.com/s', params=kw, headers=headers)
# print(response.content.decode())
#
#
# data = {'name':'lisi','age':'12'}
#
# response = requests.post('http://httpbin.org/post',data=data,headers=headers)
# print(response.content.decode())

headers = {
    "host": "mm.chinasareview.com",
    "connection": "keep-alive",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/67.0.3396.99 safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "ZH-cn,zh;q=0.9",
    "cookie": "__jsluid=28e61777c7e34ef50704f1dc59e8da96",
    "if-none-match": "f67cd360b83ed31:108f",
    "if-modified-since": "Fri, 06 Oct 2017 15:32:54 GMT",
}
response = requests.get('http://mm.chinasareview.com/wp-content/uploads/2017a/07/18/07.jpg',headers=headers)
if response.status_code == 200:
    with open('1.jpg','wb') as f:
        for block in response.iter_content(1024):
            if not block:
                break
            f.write(response.content)