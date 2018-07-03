import requests

# url = 'http://www.baidu.com/s?'
url = 'http://httpbin.org/post'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"
}
kw = {'wd': '尚硅谷'}
data = {'name': 'zhangsan', 'age': '12'}
response = requests.post(url, data=data, headers=headers)

# response = requests.get(url, headers=headers, params=kw)

print(response.text)
print(response.url)
print(response.content.decode())
# print(response.status_code)
# print(response.headers)
# print(response.cookies)
