from lxml import etree

html_obj = etree.parse('hello.html')

result_list = html_obj.xpath('//li') #获取所有的li标签文档
for result in result_list:
    print(etree.tostring(result).decode()) #序列化li标签文档并解码为html字符串

result_list = html_obj.xpath('//li/@class')  #获取所有li标签的class属性值
print(result_list)
for result in result_list:
    print(result)

result_list = html_obj.xpath('//li/a[@href="link1.html"]/text()')  #获取li标签下href属性为link1.html的a标签的文本内容
# result_list = html_obj.xpath('//li/a[@href="link1.html"]') #获取li标签下href属性为link1.html的a标签
print(result_list)
for result in result_list:
    print(result)
    print(etree.tostring(result).decode())

# result_list = html_obj.xpath('//li//span/text()')  获取li后代span标签的文本内容
result_list = html_obj.xpath('//li/a/span/text()')  #获取li下a下的span标签的文本内容
# result_list = html_obj.xpath('//li/a/text()') 获取li下a标签的文本内容，不包a标签后代标签的文本内容
for result in result_list:
    print(result)

result_list = html_obj.xpath('//li[last()]/a/@href') #获取最后一个li的a标签的href属性值
print(result_list)

result_list = html_obj.xpath('//li[last()-1]/a')  #获取最后一个的前一个li的a标签
print(result_list[0].text)

result_list = html_obj.xpath('//li[last()-2]//text()') #获取最后一个的前一个li的文本内容以及他下面所有标签的文本内容，包括
print('dddd',result_list)


result_list = html_obj.xpath('//*/@class')  #获取所有标签的class属性值
for result in result_list:
    print(result)

result_list = html_obj.xpath('//*[@class="bold"]/text()') #获取class属性值为bold的标签的文本内容

print(result_list)
result_list = html_obj.xpath('//*[contains(@href,"html")]')  #获取所有href属性值包含html的标签
for result in result_list:
    print(etree.tostring(result).decode())