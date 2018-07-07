import requests
import jsonpath
import json
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

response = requests.get(url)

text = response.text

print(text)
print(type(text))#str类型，json数据类型

#json数据类型转换成python对象（字典，列表）
text = json.loads(text)
print(type(text))
print(text)


name_city = jsonpath.jsonpath(text,"$..name")
print(name_city)

#python的对象（list） -->保存到本地 ，json库
print(type(name_city))
f = open("city.json","w")
json.dump(name_city,f,ensure_ascii=False)