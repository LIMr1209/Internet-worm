import json
list_str = [1, 2, 3, 4]
tuple_str = (1, 2, 3, 4)
dict_str = {"city": "北京", "name": "大猫"}
print(dict_str)#[1, 2, 3, 4]
print(type(dict_str))

list_str = json.dumps(list_str)
print(list_str)#[1, 2, 3, 4]
print(type(list_str))


tuple_str = json.dumps(tuple_str)
print(tuple_str)
print(type(tuple_str))

#转换成json字符串ensure_ascii=False，utf-8编码
dict_str = json.dumps(dict_str,ensure_ascii=False)
print(dict_str)
print(type(dict_str))