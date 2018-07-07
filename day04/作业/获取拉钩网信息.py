import requests
import json

url = 'https://www.lagou.com/lbs/getAllCitySearchLabels.json'

response = requests.get(url)

data = response.text

python_dict = json.loads(data)

result = python_dict.get('content').get('data').get('allCitySearchLabels')
city_list = []
for key, value in result.items():
    for i in value:
        city_list.append(i['name'])
print(city_list)

with open('city.json', 'w') as f:
    json.dump(city_list, f, ensure_ascii=False)
