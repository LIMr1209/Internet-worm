import json

from bs4 import BeautifulSoup
import re
html="""
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...daosjdasjdl;ajd;ajsda;jd</p>


"""


soup=BeautifulSoup(html,'lxml')
# print(soup.p.attrs)
#1. 得到第一个p的文本
first_p = soup.p.text
print(first_p)


# 2.得到所有p的文本

p_list = soup.find_all("p")
for p in p_list:
	print(p.string)


# 3.找到a下所有的href
a_list = soup.select('a')
for href in a_list:
	print(href['href'])

# 4.查找所有id为link3的标签内容

link = soup.select('#link3')

# print(link)
for i in link:
	print(i.string)
# 5.通过类名查找所有的类名为sister的内容

sister=soup.select('.sister')

for i in sister:
	print(i.string)


# 6.使用select，查找第2个p标签的文本内容

print(soup.select("p")[2].get_text())


# json
# 7.把dict=｛”name“:"sam"｝转化成json,
dict={"name":"sam"}

dict_json=json.dumps(dict)
print(dict_json)

# 8.将第８题　的结果转成pyton
dict_json=json.loads(dict_json)
print(dict_json)

# 9.爬取京东页面链接：
#  url="https://search.jd.com/Search?keyword=%E7%94%B5%E8%84%91&enc=utf-8&suggest=1.def.0.V16&wq=diannao&pvid=402b697940424b0cbbb5d35702b375bd"




