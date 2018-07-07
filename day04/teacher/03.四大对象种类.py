from bs4 import BeautifulSoup
from bs4.element import  Comment
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

soup = BeautifulSoup(html,"lxml")

# print(soup.title)
#Tag类型
# print(type(soup.title))

#NavigableString
# print(soup.b.string)
# print(type(soup.b.string))
#
# #BeautifulSoup
# print("--"*20)
# print(soup)
# print(type(soup))
#
# #Comment类型，本质是NavigableString
# print(soup.a.string)
# print(type(soup.a.string))
#
# print(soup.head)
# print(type(soup.head))

# print("tag的重要属性")
#
# print(soup.a)
# print(soup.a.attrs)
# #得到某个标签的所以属性
# print(type(soup.a.attrs))
# print(soup.a.attrs["href"])
# print(soup.a["class"])
# print(soup.a["id"])
# #得到标签的名称
# print(soup.a.name)
# print(soup.head.name)

# print(soup.p.string)
# print(type(soup.p.string))
#
# print(soup.p.b.string)
# print(type(soup.p.b.string))


# for p in soup.find_all(name="a"):
# 	print(p.string)


print(soup.a.attrs)
print(soup.a.name)
print(soup.p.b)





