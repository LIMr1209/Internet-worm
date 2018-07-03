import requests
url = "https://www.12306.cn/mormhweb/"

#就是请求12306网站的时候，忽略ca认证
response = requests.get(url,verify=False)

print(response.text)