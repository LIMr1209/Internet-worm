import requests

proxy= {"http": "122.72.18.35:80"}

#设置代理

response = requests.get("http://www.atguigu.com",proxies=proxy)

print(response.text)