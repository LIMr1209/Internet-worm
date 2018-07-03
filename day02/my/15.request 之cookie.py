import requests
response = requests.get('http://www.baidu.com')
cookie_jar = response.cookies
cookie_dict = requests.utils.dict_from_cookiejar(cookie_jar)
print(cookie_jar)
cookie_str =''
for item in cookie_jar:
    print(item)
    cookie_str+= item.name+':'+item.value+';'
cookie_str = cookie_str[:-1]
print(cookie_str)
print(cookie_dict)