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


soup = BeautifulSoup(html,"lxml")

# list_a_tag = soup.find_all(name="a")
# print(list_a_tag)
# for a in list_a_tag:
# 	print(a["href"])


#得到所以b字母开头的标签
# list_b_tag = soup.find_all(name=re.compile(r"^b"))
# for b in list_b_tag:
# 	print(b.name)
# 	print(b.string)


# list_b_tag = soup.find_all(["a","b","p"])
# for b in list_b_tag:
# 	print(b.name)
# 	print(b.string)


# for id  in soup.find_all(id="link1"):
# 	print(id["href"])


#内容
# for id  in soup.find_all(text="Lacie"):
# 	print(id)
# 	print(type(id))


# 得到所有前缀是http://example.com/的节点

all_link = soup.find_all(href=re.compile(r"http://example.com"))

print(all_link)

for a in all_link:
	print(a["href"])





