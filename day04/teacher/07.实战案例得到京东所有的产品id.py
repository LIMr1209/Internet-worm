from urllib3 import PoolManager,disable_warnings
from bs4 import BeautifulSoup
import re
#忽略警告
disable_warnings()

def get_product_id():

	headers = {

	"Host":"search.jd.com",
	"Connection":"keep-alive",
	"Cache-Control":"max-age=0",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	"Referer":"https://www.jd.com/",
	"Accept-Language":"zh-CN,zh;q=0.9",
	"Cookie":"PCSYCityID=1; areaId=1; xtest=2420.cf6b6759; user-key=78b0fa39-e8ec-4436-804f-4f9579c6db0c; ipLoc-djd=1-2901-4135-0.138288412; ipLocation=%u5317%u4eac; cn=0; __jdu=1597118661; pinId=tF0w3lsgbrKuuR-PW68-4Q; pin=python_afu; unick=python_afu; _tp=wmA28pFNyQS3czxsK1OIHA%3D%3D; _pst=python_afu; TrackID=1jkwkMsbITuHnXFdkxvZJAIK46_4shbaSjeMYE_8bRn5RWoH29BUmukoZd4PEd8_16uiE8CpOHYJi4tAoyLDr8Q; unpl=V2_ZzNtbRcARxUlCE9SeEpbB2JWQFURXhRFclxFXH9KDgMzUEFcclRCFXwUR1JnGFkUZwYZXEBcQB1FCHZXfBpaAmEBFl5yBBNNIEwEACtaDlwJARFeRFFGHX0KRFdLKV8FVwMTbUJTSxN1CE9TfBlsNWAzIm1BX0cRfQ92VUsYbEczXxFbQV5LEjgIQlx9GVwMYAQSbUNnQA%3d%3d; __jdv=122270672|baidu-search|t_262767352_baidusearch|cpc|32277499332_0_df51a1872b634dc9b8fa6e295bc7ebb0|1530684210612; qrsc=3; mt_xid=V2_52007VwMWWltYUlMYThlsDTIKF1QPUVJGS0hKXBliVxVQQVBWDRpVEF8MZgJGVAoNBg0ZeRpdBW4fE1RBWVZLHEsSWQVsBhRiX2hSahxIEV8AYQoQWm1YV1wY; __jda=122270672.1597118661.1530446014.1530804247.1530847742.10; __jdc=122270672; shshshfpb=0b75efa47522f0f07cef09e462f624749b4502d8c036c1e6a5b38c5921; __jdb=122270672.2.1597118661|10.1530847742; rkv=V0600; shshshfp=371fb230808abfd6f77ff94cbf7ab182; shshshfpa=8e9642e8-b96f-1567-efcd-d95cd1b080df-1530847765; shshshsID=282b94ed64f0ca04af447ab2ee79e964_2_1530847765893; 3AB9D23F7A4B3C9B=OMZA4D3H6NDE4PGRTH2FS2CQ3IDAG3WYA6D7XL7W2YMLKEB5LASEODK4CXILAXSB4YUSM4XZKJBOBGMWCCQLDZFCT4",
	}

	# url = "https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&suggest=1.his.0.0&wq=&pvid=11923d52a1ac40ab8b1dab03663f9d6c"
	url = "https://search.jd.com/Search?keyword=%E5%88%AE%E8%83%A1%E5%88%80&enc=utf-8&wq=%E5%88%AE%E8%83%A1%E5%88%80&pvid=58ba4211765e438196beeb395f420ffc"
	#创建PoolManager对象
	http = PoolManager()
	#添加请求信息
	response = http.request("get",url,headers=headers)
	#得到请求回来的数据
	html = response.data.decode("utf-8")
	print(html)

	soup = BeautifulSoup(html,"lxml")

	all_link = soup.find_all(href=re.compile(r"//item.jd.com/"))

	#装所以链接的列表
	links = []
	#所以的id放在这里
	id_list = []

	for link in all_link:
		link = link["href"]
		print(link)
		links.append(link)


	#去除重复
	# print(links)
	links = list(set(links))
	# print(links)

	#获取id
	for link in links:
		id = link.replace("//item.jd.com/","").replace(".html","").replace("#comment","")
		print(id)
		id_list.append(id)


	# print(id_list)
	id_list = list(set(id_list))
	# print(id_list)
	return  id_list


if __name__ == "__main__":
	list_id = get_product_id()
	print(list_id)


