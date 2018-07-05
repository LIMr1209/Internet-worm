from urllib.request import Request,urlopen,URLError
import re
class Spider(object):

	def save_text(self,text):
		#在文本末尾追加"a"，文本类型
		with open("内涵段子.txt","a") as f:
			f.write(text)


	def handle_data(self,list):
		#循环
		for item in list:
			#取出每一条
			item = item.replace("<p>","").replace("</p>","").replace("<br />","").replace('&ldquo;','"').replace('&rdquo;','"').replace('&hellip;',"...")
			print(item)
			self.save_text(item)

	def downlad_page(self,page):
		"""请求某页面的数据"""

		url = "https://www.neihan8.com/article/list_5_"+str(page)+".html"
		headers = {
			"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
		}
		try:
			request = Request(url,headers=headers)
			response = urlopen(request)
			data = response.read()
			return data
		except URLError as e:
			print("报错了",e)
		return ""


	def start(self):
		print("""爬取内涵吧开始了...""")
		#爬取从第1页开始
		self.page = 1

		while True:

			# cmd = input("按任意建继续，退出输出：q")
			# if cmd == "q":
			# 	break
			print("正则爬取-----------------------------------------：",self.page,"页")

			if self.page <= 506:
				#GB18030>GBK>GB2312
				html = self.downlad_page(self.page).decode("GBK")
				# print(html)
				#使用正则表达式摘取数据
				pattern = re.compile(r'<div class="f18 mb20">(.+?)</div>',re.S)
				#lieb
				list_neihans = pattern.findall(html)
				print(list_neihans)

				#出来数据的方法
				self.handle_data(list_neihans)
				# print(list_neihans)

				self.page += 1
			else:
				break




if __name__ == "__main__":
	Spider().start()