import requests


url = "http://192.168.28.123:8080/hello"
url = "http://httpbin.org/post"

data = {
	"name":"zhangsan",
	"password":"afu123456"
}
response = requests.post(url,data=data)

print(response.text)