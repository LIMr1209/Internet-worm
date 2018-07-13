import requests
from  lxml import etree

response=requests.get("http://www.baidu.com")
print(response.content.decode())

soup=etree.HTML(response.content.decode())
a=soup.xpath('//span[@class="btn_wr"]')
print(a)