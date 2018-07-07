import json
#json数据类型的字符串
#json类型的数组
json_array = "[1,2,3,4]"

#json类型的对象,里面要是双引号
json_object = '{"name":"zhangsan","age":"18"}'
print(json_array)
print(type(json_array))#str

print(json_object)
print(type(json_object))#dict or str

#把json类型的数组转换成python对象里的list
json_array = json.loads(json_array)
print(json_array)
print(type(json_array))#str or list

json_object = json.loads(json_object,encoding="utf-8")
print(json_object)
print(type(json_object))#dict
