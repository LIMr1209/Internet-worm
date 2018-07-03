import requests

session = requests.session()
url = 'http://www.renren.com/PLogin.do'
data = {'email': "aaa1058169464@126.com", 'password': 'aaa1058169464'}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

}
response = session.post(url, data=data, headers=headers)
print(response.text)
url1 = "http://www.renren.com/881820831/profile"
response = session.get(url1, headers=headers)
print(response.text)
