import json
import requests
from lxml import etree

url = "https://www.qiushibaike.com/8hr/page/1/"
response = requests.get(url)
html = response.content.decode('utf-8')
html_obj = etree.HTML(html)
node_list = html_obj.xpath('//div[contains(@id,"qiushi_tag")]')
items = []
for node in node_list:
    item = {}
    user_image = node.xpath('./div/a/img/@src')
    user_name = node.xpath('./div/a/h2/text()')
    content = node.xpath('./a//span/text()')
    num = node.xpath('./div//i/text()')
    if len(user_image) > 0:
        user_image = user_image[0]
        item['user_image'] = user_image
    if len(user_name) > 0:
        user_name = user_name[0]
        item['user_name'] = user_name.strip()
    content = ''.join(content)
    item['content'] = content.strip()
    love_num = num[0]
    item['love_num'] = love_num
    comment_num = num[1]
    item['comment_num'] = comment_num
    print(item)
    items.append(item)
with open('qiushi.txt','w',encoding='utf-8') as f:
    json.dump(items,f,ensure_ascii=False)
