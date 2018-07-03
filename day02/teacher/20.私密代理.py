import requests

proxy= {"http": "http://trygf521:a4c4avg9@114.67.224.159:16816"}
#设置代理

response = requests.get("http://www.atguigu.com",proxies=proxy)

print(response.text)