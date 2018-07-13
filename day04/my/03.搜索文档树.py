from bs4 import BeautifulSoup
import re

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup = BeautifulSoup(html,'lxml')

a_list = soup.find_all(name='a') #找到所有标签名为a的标签
for a in a_list:
    print(a.string)
a_list = soup.find_all(href=re.compile(r'http://example.com/'))  #找到所有的href属性值能匹配正则的标签
for a in a_list:
    print(a['href'])
print(soup.find_all(text=re.compile("Dormouse"))) #找到所有的文本内容能匹配正则的标签
print(soup.find_all(id='link2'))  #找到id为link2的标签
