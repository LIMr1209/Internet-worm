import requests
# url = "http://www.atguigu.com"

kw = input("请输入你要搜索的内容：")

kw = {"wd":kw}
#
# url = "https://www.baidu.com/s?"
url = "http://192.168.28.123:8080/hello"

headers = {
	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
}
#get请求
response = requests.get(url,headers=headers,params=kw)
#网页内容


#解码好的数据
# print(response.text)
#response.content类型是bytes类型
print(response.content.decode("utf-8"))

#得到cookie信息
print(response.cookies)
#得到请求的url
print(response.url)
#得到状态码
print(response.status_code)