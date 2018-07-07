from bs4 import BeautifulSoup

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

soup = BeautifulSoup(html, 'lxml')

tag_list = soup.body.contents  # 返回列表
# print(tag_list)
# print(type(tag_list))
# print(tag_list[0])  # 空白
# for tag in tag_list:
#     print(tag)  # 空白,和标签
#     print(type(tag))  # 空白类型<class 'bs4.element.NavigableString'>，标签类型<class 'bs4.element.Tag'>


tag = soup.body.children  # 返回迭代器
print(tag)
print(next(tag))  # 空白
for i in tag:
    # 迭代了一次，从第二次开始
    print(i)  # 空白,和标签
    print(type(i))  # 空白类型<class 'bs4.element.NavigableString'>，标签类型<class 'bs4.element.Tag'>
