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
# #查找p标签下 id为link3的所以标签
# list_p =soup.select("p #link3")
# # print(list_p)
# for p in list_p:
# 	print(p.string)


#查找p标签下 类名为sister的所以标签
# list_p =soup.select("p .sister")
# # print(list_p)
# for p in list_p:
# 	print(p)
# 	# print(p.string)


# list_p =soup.select('a[href="http://example.com/elsie"]')
# # print(list_p)
# for p in list_p:
# 	print(p)
# 	# print(p.string)



list_p = soup.select('title')
print(list_p[0].get_text())
# print(list_p)
for p in list_p:
	print(p.string)
	print(p.get_text())
	# print(p.string)