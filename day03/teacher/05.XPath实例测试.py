from lxml import etree

html = etree.parse("./hello.html")

#3.5.1. 获取所有的 <li> 标签
# li_list = html.xpath("//li")

# li_list = html.xpath("//li")
# for li in li_list:
# 	result = li.xpath("./a/text()")
# 	print(result)


#继续获取<li> 标签的所有 class属性
# li_list = html.xpath("//li/@class")
# print(li_list)

#继续获取<li>标签下hre f为 link1.html 的 <a>标签
# li_list = html.xpath('//li/a[@href="link1.html"]')
# # li_list = html.xpath('//li/a[@href="link1.html"]/text()')
# print(li_list)

#获取<li> 标签下的所有 <span> 标签

# li_list = html.xpath('//li//span')
# print(li_list)


# 获取 <li> 标签下的<a>标签里的所有 class
# li_list = html.xpath('//li/a//@class')
# print(li_list)

#获取最后一个 <li> 的 <a> 的 href

# li_list = html.xpath('//li[last()]/a/@href')
# print(li_list)

# 获取倒数第二个元素li的内容,也就是fourth item
# li_list = html.xpath('//li[last()-1]/a/text()')
# print(li_list)
#
# li_list = html.xpath('//li[last()-1]/a')
# print(li_list[0].text)

#3.5.8. 获取 class 值为 bold 的标签名
li_list = html.xpath('//*[@class="bold"]')
print(li_list)

# 注意//li/@class和//*/@class不一样

#li下
li_list = html.xpath('//li/@class')
print(li_list)

#*任意
li_list = html.xpath('//*/@class')
print(li_list)


