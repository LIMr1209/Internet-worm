import requests
from bs4 import BeautifulSoup
import json

url = 'http://hr.tencent.com/position.php?&start=10#a'

headers = {
    "Host": "hr.tencent.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "_ga=GA1.2.352190501.1523238701; pgv_pvi=2483341312; PHPSESSID=0ifm5pggbmotlaj6qhjrb63uv1",
}

response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'lxml')

even = soup.select('.even')
odd = soup.select('.odd')

all_tags = even + odd
items = []
for tag in all_tags:
    item = {}
    name = tag.select('td')[0].a.get_text()
    data_link = tag.td.a['href']
    job_category = tag.select('td')[1].get_text()
    recruit_number = tag.select('td')[2].get_text()
    address = tag.select('td')[3].get_text()
    publish_time = tag.select('td')[4].get_text()
    item['name'] = name
    item['data_link'] = data_link
    item['job_category'] = job_category
    item['recruit_number'] = recruit_number
    item['address'] = address
    item['publish_time'] = publish_time
    items.append(item)

with open('招聘信息.json','w') as f:
    json.dump(items,f,ensure_ascii=False)



