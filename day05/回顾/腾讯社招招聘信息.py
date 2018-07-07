import requests
import json
from bs4 import BeautifulSoup


url = 'http://hr.tencent.com/position.php?&start=10#a'
headers = {
    "Host": "hr.tencent.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "_ga=GA1.2.352190501.1523238701; pgv_pvi=2483341312; PHPSESSID=9hij7vpv48moadte5322d5kog7; pgv_si=s5535851520",
}

response = requests.get(url, headers=headers)

html = response.content.decode()

soup = BeautifulSoup(html,'lxml')

odd = soup.select('.odd')

even = soup.select('.even')

items = []

all_tr = odd+even
for tr in all_tr:
    item = {}
    user_name = tr.td.a.get_text()
    print(user_name)
    data_link = tr.td.a['href']
    print(data_link)
    address = tr.select('td')[3].get_text()
    print(address)
    item['user-name'] = user_name
    item['data_link'] = data_link
    item['address'] = address
    items.append(item)
print(items)

with open('job.json','w') as f:
    json.dump(items,f,ensure_ascii=False)