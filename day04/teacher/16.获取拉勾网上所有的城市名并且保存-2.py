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

result = text.get("content").get("data").get("allCitySearchLabels")
print(result)

for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

	#判断AB是否在result
	if letter in result:

		for address in result.get(letter):
			name = address.get("name")
			print(name)
