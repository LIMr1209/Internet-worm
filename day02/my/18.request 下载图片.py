import requests

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

with open('1.jpg', 'wb') as f:
    f.write(response.content)
    print('保存成功')
