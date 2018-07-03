import requests

response = requests.get("http://www.baidu.com")

cookies = response.cookies


print(requests.utils.dict_from_cookiejar(cookies))