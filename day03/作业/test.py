import requests
from lxml import etree

response = requests.get('http://www.baidu.com')

print(response.content.decode())
print(response.content)

html_obj = etree.HTML(response.content.decode())
print(etree.tostring(html_obj))
print(type(html_obj))
html_obj = etree.HTML(response.content)
print(etree.tostring(html_obj))

# HTML方法会把html字符串或者html的bytes类型的文件转化成<class 'lxml.etree._Element'>，且补全html和body标签
# 然后etree.tostring会把<class 'lxml.etree._Element'>转换成bytes类型的html文件
