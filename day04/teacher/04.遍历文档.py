
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


soup = BeautifulSoup(html,"lxml")

# print(soup.a.contents)
# print(soup.a.contents[0])

# for a in soup.find_all("a"):
# 	print(a.contents)


# print(soup.p.children)
# #得到所以自己的孩子
# for a in soup.p.children:
# 	print(a)

# for a in soup.find_all("p"):
#
# 	for i in a.children:
# 		print(i)
#



for a in soup.find_all("body"):

	for i in a.descendants:
		print(i)



