from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<a>haha</a>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""

soup = BeautifulSoup(html, 'lxml')

p_list = soup.select('p')
for p in p_list:
    print(p.get_text())  # 取不到注释内容，可以取到嵌套标签的所有文本内容

class_list = soup.select('.sister')  # 类选择器
for a in class_list:
    print(a.get_text())  # 取不到注释内容，为空

b = soup.select('#link1')  # id选择器

c = soup.select('p .sister')  # 后代选择器

d = soup.select('body > a')  # 子选择器

for x in d:
    print(x.get_text())

attr_list = soup.select('a[class="sister"]')  # 属性选择器
for a in attr_list:
    print(a.get_text())  # 取不到注释内容，为空

print(soup.select('a[href="http://example.com/elsie"]'))  # 属性选择器


s = 'hahah'

print(s.__contains__('h'))
