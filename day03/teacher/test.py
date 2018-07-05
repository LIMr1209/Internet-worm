from lxml import etree
html = etree.parse("./hello.html")

# html = etree.tostring(html)


li_list = html.xpath("//li")
for li in li_list:
	result = li.xpath("./a/text()")
	print(result)


result = html.xpath('//li/@class')
print(result)

result = html.xpath('//li//a/text()')
print(result)
result = html.xpath('//li//span')
print(result)

result = html.xpath("//li/a//@class")
print(result)

result = html.xpath("//li[last()]/a/@href")
print(result)
result = html.xpath("//li[last()-1]/a/text()")
print(result)
result = html.xpath("//*[@class='bold']")
print(result)

result = html.xpath('//*/@class')

print(result)

result = html.xpath("//li[contains(@class,'item')]")
print(result)
