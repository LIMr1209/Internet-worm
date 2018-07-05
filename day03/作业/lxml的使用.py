from lxml import etree

html_obj = etree.parse('hello.html')
print(type(html_obj))
html = etree.tostring(html_obj).decode()
# print(html)

full_html_obj = etree.HTML(html)

full_html = etree.tostring(full_html_obj).decode()
# print(full_html)

result_list = html_obj.xpath('//li')
for result in result_list:
    print(etree.tostring(result).decode())

result_list = html_obj.xpath('//li/@class')

for result in result_list:
    print(result)

# result_list = html_obj.xpath('//li/a[@href="link1.html"]/text()')
result_list = html_obj.xpath('//li/a[@href="link1.html"]')
for result in result_list:
    # print(result)
    print(etree.tostring(result).decode())

# result_list = html_obj.xpath('//li//span/text()')
result_list = html_obj.xpath('//li/a/span/text()')
# result_list = html_obj.xpath('//li/a/text()')
for result in result_list:
    print(result)

result_list = html_obj.xpath('//li[last()]/a/@href')
print(result_list)

result_list = html_obj.xpath('//li[last()-1]/a')
print(result_list[0].text)

result_list = html_obj.xpath('//li[last()-2]//text()')
print(result_list)


result_list = html_obj.xpath('//*/@class')
for result in result_list:
    print(result)

result_list = html_obj.xpath('//*[@class="bold"]/text()')
print(result_list)
