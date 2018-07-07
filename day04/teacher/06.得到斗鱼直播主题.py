import requests
from bs4 import BeautifulSoup

url = 'https://www.douyu.com/directory/all'

headers = {
"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}

response = requests.get(url,headers=headers)

text = response.text
# print(text)

soup = BeautifulSoup(text,"lxml")

#得到直播主题
all_h3 = soup.find_all(name="h3")
for h3 in all_h3:
	print("斗鱼直播主题====",h3.string.strip())

