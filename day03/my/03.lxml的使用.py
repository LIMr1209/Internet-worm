from lxml import etree

html = etree.parse('./hello.html')
print(html)
html = etree.tostring(html)
# # print(html.decode())
html = etree.HTML(html)
html = etree.tostring(html)
print(html)
print(html.decode())
# result = html.xpath('//li')
# for item in result:
#     print(etree.tostring(item).decode())
#
# result = html.xpath('//li/@class')
# print(result)
#
# result = html.xpath('//li/a[@href="link1.html"]/text()')
# print(result)
#
# result = html.xpath('//li//span')
#
# for item in result:
#     print(etree.tostring(item).decode())
#
# result = html.xpath('//li[last()]/a/@href')
# print(result)
#
# result = html.xpath('//li[last()-1]/a')
# print(result[0].text)
#
# result = html.xpath('//li[last()-1]//text()')
# print(result)
#
# result = html.xpath('//*[@class="bold"]')
# print(result[0].tag)
# print(result[0].text)
#
#
# result = html.xpath('//div[contains(@id,"qiushi_tag_")]')