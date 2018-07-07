import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.douyu.com/directory/all')
# content = response.content
# content = response.text     #这三个html都行
content = response.content.decode()

soup = BeautifulSoup(content,'lxml')

# h3_list = soup.find_all(name='h3')
h3_list = soup.select('h3')
for h3 in h3_list:
    print(h3.string.strip())