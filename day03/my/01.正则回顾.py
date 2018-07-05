import re

# mathch
# s = 's python'
# pattern = re.compile(r'python')
# result = pattern.match(s,2)
# # result = pattern.match(s)
# print(result)
# print(result.group())

# search

# s = 'python hello python '
# pattern = re.compile(r'python')
# result  = pattern.search(s,6)
# print(result)
# print(result.group())

# findall
# s = 'python11 hello21 python34 '
# pattern = re.compile(r'(\d+)')
# result = pattern.findall(s)
# print(result)

# finditer

# s = 'python11 hello21 python34 '
# pattern = re.compile(r'(\d+)')
# result = pattern.finditer(s)
# print(result)
# for i in result:
#     print(i)
#     print(i.group())

# split

s= 'admin123haha123hehe123'
pattern = re.compile(r'(\d+)')
result = pattern.split(s)
print(result)


#sub
# ? + *
#贪婪和非贪婪
#\w  \W  \d  \D \s \S  .