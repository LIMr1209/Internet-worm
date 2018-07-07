import json

# json数组转python列表
json_array = '[1,2,3,4]'
print(type(json_array))
# python_list = json.loads(json_array)
# 读取json文件并json数组转python列表
fp = open('json_array.json','r')
python_list = json.load(fp)
print(python_list)
print(type(python_list))

# json对象转python字典
json_obj = '{"name":"张三","age":12}'
print(type(json_obj))
# python_dict = json.loads(json_obj)
# 读取json文件并json对象转python字典
fp = open('json_obj.json','r')
python_dict = json.load(fp)
print(python_dict)
print(type(python_dict))

# python列表转json数组
# json_array1 = json.dumps(python_list)
# python列表转json数组并写入文件
fp = open('json_array.json','w')
json_array1 = json.dump(python_list,fp)
print(type(json_array1))
print(json_array1)
# python字典转json对象
# json_obj1 = json.dumps(python_dict, ensure_ascii=False)  # 有中文 填入ensure_ascii=False
# python字典转json对象并写入文件
fp = open('json_obj.json','w')
json_obj1 = json.dump(python_dict, fp,ensure_ascii=False)
print(type(json_obj1))
print(json_obj1)
# python元组转json列表
python_tuple = (1, 2, 3, 4)
json_array2 = json.dumps(python_tuple)
print(type(json_array2))
print(json_array2)


