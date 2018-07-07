import requests
import jsonpath
import json
url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

response = requests.get(url)
content = response.text
print(content)

text = json.loads(content)
print(text)
print(type(text))

# name_city = jsonpath.jsonpath(text,"$..name")
# print(type(name_city))
# print(name_city)
# print(len(name_city))
# city = json.dumps(name_city,ensure_ascii=False)
# print(type(city))

result = text.get('content').get('data').get('allCitySearchLabels')
print(result)
city_list = []
for key,value in result.items():
    for i in value:
        city = i.get("name")
        city_list.append(city)

print(len(city_list))
city = json.dumps(city_list,ensure_ascii=False)
with open('city.json','w') as f:
    f.write(city)
