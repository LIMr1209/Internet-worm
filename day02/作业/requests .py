import requests

headers = {
    "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/67.0.3396.99 safari/537.36",
}
kw = {'wd': '尚硅谷'}
response = requests.get('http://www.baidu.com/s?', params=kw, headers=headers)
print(response.content.decode())

data = {
    'name': 'zhangsan',
    'age': '18'
}
response = requests.post('http://httpbin.org/post',data=data,headers=headers)
print(response.content.decode())


