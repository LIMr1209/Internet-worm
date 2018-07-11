import requests

url = "http://www.atguigu.com/teacher.shtml"
response = requests.get(url)
print(response.url)
print(response.content)
print(type(response.content))
print(response.text)