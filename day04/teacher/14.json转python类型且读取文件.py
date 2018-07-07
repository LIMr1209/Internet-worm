import json

f = open("dict_str.json")

result = json.load(f)
print(result)


f = open("list_str.json")

result = json.load(f)
print(result)

f = open("tuple_str.json")

result = json.load(f)
print(result)