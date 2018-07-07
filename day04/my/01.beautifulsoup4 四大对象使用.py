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

# Tag

# print(soup.html)
# print(soup.prettify())
# print(soup.p)  # 找到第一个p标签
# print(type(soup.p))  # <class 'bs4.element.Tag'>
# print(soup.name)  # document
# print(soup.p.name)
# print(soup.p.b.name)
# print(soup.head.name)  # 标签名  head
# print(soup.p.attrs)
# print(soup.p.attrs['class'])
# print(soup.p['class'])
# print(soup.p.get('class'))
# soup.p['class'] = 'haha'
# print(soup.p)
# print(soup.prettify())
# del soup.p['class']
# print(soup.prettify())

# NavigableString

print(soup.p.string)
print(type(soup.p.string))
p_list = soup.find_all('p')
for p in p_list:
    print(p.string)
a_list = soup.find_all(name='a')
for a in a_list:
    print(a.string)

print(soup.attrs)

print(soup.a.string)
print(type(soup.a.string))
