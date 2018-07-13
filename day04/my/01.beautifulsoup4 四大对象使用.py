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

# Tag 通俗点讲就是 HTML 中的一个个标签，例如：

print(soup.html)  # 字符串输出html
print(soup.prettify())  # 美化的字符串输出html
print(soup.p)  # html的第一个p标签
print(type(soup.p))  # <class 'bs4.element.Tag'>
print(soup.p.name)  # html的第一个p标签的标签名
print(soup.p.b.name)  # html的第一个p标签的第一个b标签的标签名
print(soup.head.name)  # 标签名  head
print(soup.p.attrs)  # p标签的属性值 {'class': ['title'], 'name': 'dromouse'}
print(soup.p.attrs['class'])  # p标签的属性 class的值
print(soup.p['class'])  # p标签的属性 class的值
print(soup.p.get('class'))  # p标签的属性 class的值
soup.p['class'] = 'haha'  # 修改p标签的属性
del soup.p['class']  # 删除P标签的属性class

# NavigableString 标签的内容 .string

print(soup.p.string)  # p标签的文本
print(type(soup.p.string))  # <class 'bs4.element.NavigableString'>
p_list = soup.find_all('p')  # 找到所有p标签
for p in p_list:
    print(p.string)  # 所有p标签的文本  <class 'bs4.element.NavigableString'>
a_list = soup.find_all(name='a')  # 找到所有a标签
for a in a_list:
    print(a.string)  # 所有a标签的文本  <class 'bs4.element.NavigableString'>

# BeautifulSoup 对象表示的是一个文档的内容。大部分时候,可以把它当作 Tag 对象，是一个特殊的 Tag，我们可以分别获取它的类型，名称，以及属性来感受一下
print(type(soup))  # <class 'bs4.BeautifulSoup'>
print(type(soup.name))  # <class 'str'>
print(soup.name)  # [document]
print(soup.attrs)  # 文档本身的属性为空{}

# Comment 对象是一个特殊类型的 NavigableString 对象，其输出的内容不包括注释符号。
print(soup.a.string)  # Elsie
print(type(soup.a.string))  # <class 'bs4.element.Comment'>
# a 标签里的内容实际上是注释，但是如果我们利用 .string 来输出它的内容时，注释符号已经去掉了。
