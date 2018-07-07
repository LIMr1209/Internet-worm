import json
list_str = [1, 2, 3, 4]
tuple_str = (1, 2, 3, 4)
dict_str = {"city": "北京", "name": "大猫"}
print(dict_str)#[1, 2, 3, 4]
print(type(dict_str))

fp = open("list_str.json",'w')

list_str = json.dump(list_str,fp)
print(list_str)#[1, 2, 3, 4]
print(type(list_str))

fp = open("tuple_str.json",'w')
tuple_str = json.dump(tuple_str,fp)
print(tuple_str)
print(type(tuple_str))
#
#转换成json字符串ensure_ascii=False，utf-8编码
fp = open("dict_str.json",'w')
dict_str = json.dump(dict_str,fp,ensure_ascii=False)
print(dict_str)
print(type(dict_str))