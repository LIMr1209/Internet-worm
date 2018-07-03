import urllib.request
url = 'http://www.baidu.com'


response = urllib.request.urlopen(url)
# response = urllib.request.urlopen(url,data='name=zhangsan'.encode())


data = response.read()
#读取内容解码
print(data.decode())