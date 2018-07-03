import requests

# url = "http://www.atguigu.com/images/logo.jpg"
# url = "http://www.atguigu.com/pics1/teacherbanner.jpg"
url = "http://mm.chinasareview.com/wp-content/uploads/2017a/07/18/07.jpg"
headers = {
"Host":"mm.chinasareview.com",
"Connection":"keep-alive",
"Cache-Control":"max-age=0",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Accept-Encoding":"gzip, deflate",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"__jsluid=14600d3c4078768577d30aceeb875172",
"If-None-Match":"f67cd360b83ed31:108f",
"If-Modified-Since":"Fri, 06 Oct 2017 15:32:54 GMT",
}
#get请求
response = requests.get(url,headers=headers)

print(response.status_code)
#保存图片
if response.status_code == 200:#200成功
	with open("logo.jpg",'wb') as f:
		f.write(response.content)


print("图片下载完成")