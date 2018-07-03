#coding=utf-8
#在python2中使用urllib2网络请求
# import urllib2
import urllib.request

# url = "http://www.atguigu.com/teacher.shtml"

url = "http://192.168.28.85:8080/hello"

#根据url请求网站
# request = urllib2.urlopen(url)
# request = urllib.request.urlopen(url)

#post请求
request = urllib.request.urlopen(url,data="name=afu&age=33".encode())
#读取还回回来的所以数据
content = request.read()

print(content.decode())


