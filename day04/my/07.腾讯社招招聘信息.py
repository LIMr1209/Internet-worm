import requests
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
    "Cookie": "_ga=GA1.2.352190501.1523238701; pgv_pvi=2483341312; PHPSESSID=bv9dj2poc52ovcncaj4n3hdkh2; pgv_si=s9641553920",
}

response = requests.get(url, headers=headers)
html = response.text
# html = response.content        #这三个html都行
# html = response.content.decode()
soup = BeautifulSoup(html, 'lxml')

even = soup.select('tr[class="even"]')
odd = soup.select('tr[class="odd"]')

all_tags = even + odd
# print(all_tags)

items = []

for tr in all_tags:
    item={}
    name = tr.td.a.get_text()
    data_link = tr.td.a['href']
    job_category = tr.select('td')[1].get_text()
    recruit_number = tr.select('td')[2].get_text()
    address = tr.select('td')[3].get_text()
    publish_time = tr.select('td')[4].get_text()
    item['name'] = name
    item['data_link'] = data_link
    item['job_category'] = job_category
    item['recruit_number'] = recruit_number
    item['address'] = address
    item['publish_time'] = publish_time
    items.append(item)
print(items)

with open('json.txt','w') as f:
    f.write(str(items))