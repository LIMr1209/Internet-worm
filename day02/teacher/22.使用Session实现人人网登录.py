import requests

# 得到session
session = requests.session()

url = "http://www.renren.com/PLogin.do"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}

data = {
    "email": "yangguangfu2017@163.com",
    "password": "afu123456"
}

response = session.post(url, data=data, headers=headers)

print(response.text)

print("--" * 200)

# 如果登录成功后
response = session.get("http://www.renren.com/881820831/profile")

print(response.text)
