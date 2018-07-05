from lxml import etree

html = etree.parse("./hello.html")
#<lxml.etree._ElementTree object at 0x7f60de3186c8>
print(html)

html = etree.tostring(html)
print(html.decode())

html = etree.HTML(html)
print(html)

html = etree.tostring(html)
print(html.decode())
