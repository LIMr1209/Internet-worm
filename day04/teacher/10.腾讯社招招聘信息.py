import requests
from bs4 import BeautifulSoup


def get_tencent():


	url = 'https://hr.tencent.com/position.php?&start=10'

	headers = {
	"Host":"hr.tencent.com",
	"Connection":"keep-alive",
	"Cache-Control":"max-age=0",
	"Upgrade-Insecure-Requests":"1",
	"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
	"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
	# "Accept-Encoding":"gzip, deflate, br",
	"Accept-Language":"zh-CN,zh;q=0.9",
	"Cookie":"pgv_pvi=5930866688; pt2gguin=o0541433511; ptcz=ae2afbca1b0c537d3e9f19a0dadd9bfd56ae17b10a77ef55de6f129a34340bc4; PHPSESSID=gdjunlpqfl5eg5uqu8hn1qq151; pgv_si=s9775328256",
	}

	response = requests.get(url,headers=headers)
	text = response.text
	# print(text)

	soup = BeautifulSoup(text,"lxml")

	odd = soup.select('tr[class="odd"]')
	# print(odd)

	even = soup.select('tr[class="even"]')

	#匹配的结果相加
	all_tag_tr = odd + even
	# print(all_tag_tr)
	#职位
	list_postion = []

	for tr in all_tag_tr:

		item = {}


		# 职位名称（name）
		name = tr.td.a.string
		# 连接（data_link）
		data_link = tr.td.a["href"]
		# 职位类别(job_category)
		job_category = tr.select("td")[1].string
		# 招聘人数( recruit_number)
		recruit_number = tr.select("td")[2].string
		# 工作地点(address)
		address = tr.select("td")[3].string
		# 发布时间(publish_time)
		publish_time = tr.select("td")[4].string

		item["name"] = name
		item["data_link"] = data_link
		item["job_category"] = job_category
		item["recruit_number"] = recruit_number
		item["address"] = address
		item["publish_time"] = publish_time


		print(item)
		list_postion.append(item)


	#保存到本地
	with open("json.txt",'w') as f:
		#保存之前要转换成str10.类型
		f.write(str(list_postion))


if __name__ == "__main__":
	get_tencent()