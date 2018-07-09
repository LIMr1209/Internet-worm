from lxml import etree
from queue import Queue
from threading import Thread,Lock
import time
import requests
import json

#是否退出采集线程True,退出，False不退出
crawl_exit = False
parse_exit = False
class CrawlThread(Thread):
	"""采集线程"""
	def __init__(self,thread_name,page_queue,data_queue):
		super(CrawlThread,self).__init__()
		self.thread_name = thread_name
		self.page_queue = page_queue
		self.data_queue = data_queue
		self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"}

	def run(self):

		while not crawl_exit:
			try:
				page = self.page_queue.get(block=False)
				url = "https://www.qiushibaike.com/8hr/page/"+str(page)+"/"
				print("%s开始采集%s页" % (self.thread_name,url))
				response = requests.get(url,headers=self.headers)
				#把请求回来的数据放入
				self.data_queue.put(response.text)
				time.sleep(2)
			except Exception as e:
				# print(e)
				# print(self.thread_name)
				pass

class ParseThread(Thread):
	"""解析线程"""
	def __init__(self,thread_name,filename,data_queue,lock):
		super(ParseThread,self).__init__()
		self.thread_name = thread_name
		self.filename = filename
		self.data_queue = data_queue
		self.lock = lock


	def handle_data(self,html):
		# xpath获取数据
		html = etree.HTML(html)
		# 把数据加入列表
		items = []
		# 得到所以的节点
		node_list = html.xpath('//div[contains(@id,"qiushi_tag")]')
		for node in node_list:
			# 字典
			item = {}
			items.append(item)  # 可以
			# 遍历每个节点，从节点取出用户头像，和用户，段子，点赞和评论数
			user_image = node.xpath('./div/a/img/@src')
			# 用户名
			user_name = node.xpath('./div/a/h2/text()')
			# 段子
			content = node.xpath('./a/div/span/text()')
			# 点赞
			dianzhan = node.xpath('./div[@class="stats"]/span/i/text()')
			# 评论
			commont = node.xpath('./div[@class="stats"]/span/a/i/text()')

			if len(user_image) > 0:
				iamge_url = user_image[0]
				item["iamge_url"] = iamge_url

			# print(iamge_url)

			if len(user_name) > 0:
				user_name = user_name[0]
				item["user_name"] = user_name
			# print(user_name)

			if len(content) > 0:
				content = "".join(content)
				item["content"] = content
			# print(content)

			if len(dianzhan) > 0:
				dianzhan = dianzhan[0]
				# print(dianzhan)
				item["dianzhan"] = dianzhan

			if len(commont) > 0:
				commont = commont[0]
				# print(commont)
				item["commont"] = commont


		with self.lock:
			json.dump(items,self.filename,ensure_ascii=False)
		print(items)
		print(type(items))


	def run(self):

		while not parse_exit:
			try:
				#从队列获取采集采集线程请求回来的数据
				html = self.data_queue.get(block=False)
				print("%s开始解析" % (self.thread_name))
				self.handle_data(html)
				time.sleep(2)
			except Exception as e:
				# print(e)
				# print(self.thread_name)
				pass
def main():
	global crawl_exit
	global parse_exit

	#锁，开和关
	lock = Lock()


	#装页码的队列1,2,3,4,...9,10
	page_queue = Queue(10)
	for page in range(1,11):
		#添加页面
		page_queue.put(page)



	#用户装数据的队列
	data_queue = Queue()
	#线程名称
	crawl_thread_names = ["采集线程1","采集线程2","采集线程3"]
	# 用户装采集线程实例对象的
	crawl_threads = []
	#让主线程等待采集线程结束，用采集线程实例对象

	for thread_name in crawl_thread_names:
		#线程的实例对象
		thead = CrawlThread(thread_name,page_queue,data_queue)
		thead.start()#启动线程
		crawl_threads.append(thead)

	#保存数据到该文件
	filename = open("糗事.json","w")

	# 线程名称
	parse_thread_names = ["解析线程1", "解析线程2", "解析线程3"]
	# 用户装解析线程实例对象的
	parse_threads = []
	# 让主线程等待采集线程结束，用解析线程实例对象

	for thread_name in parse_thread_names:
		# 线程的实例对象
		thead = ParseThread(thread_name, filename, data_queue,lock)
		thead.start()  # 启动线程
		parse_threads.append(thead)

	#判断所以采集的是都已经采集
	while not page_queue.empty():
		#页面是否都被采集，如果没有都被采集，就做死循环
		pass
	# 采集线程停止,注意定义成全局变量，否则修改不起作用
	crawl_exit = True

	#彻底等待采集线程结束--可以去掉
	for thread in crawl_threads:
		thread.join()#让主线程等待子线程结束



	# 判断所以数据是否解析完成
	while not data_queue.empty():
		# 数据是否都被解析，如果没有都被解析完成，就做死循环
		pass
	# 解析线程停止,注意定义成全局变量，否则修改不起作用
	parse_exit = True

	# 彻底等待采集线程结束--可以去掉
	for thread in parse_threads:
		thread.join()  # 让主线程等待子线程结束

	with lock:
		filename.close()

	print("主线程结束。。。。")



if __name__ == "__main__":
	main()