import requests
import random

# server = [
#     {'http': '118.190.95.43:9001'},
#     {'http': '223.145.228.124:6666'},
# ]
# server = random.choice(server)
server = {'http': 'http://trygf521:a4c4avg9@114.67.224.159:16816/'}
# {'http':'http//用户名:密码@ip:端口/'}
response = requests.get('http://www.baidu.com', proxies=server)
# print(response.text)
print(response.content.decode())
