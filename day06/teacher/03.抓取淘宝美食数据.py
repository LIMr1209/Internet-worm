from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import re
from bs4 import BeautifulSoup
SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']
#全局变量

#无界面的浏览器
options = Options()
options.add_argument("--headless")
#代表的是浏览器
driver = webdriver.Chrome(service_args=SERVICE_ARGS,options=options)

#设置浏览器的窗口大小
# driver.set_window_size(width=1360, height=768)
#第一个参数是传入driver,第二个参数是等待时间
wait = WebDriverWait(driver,5)

def next_page(page):
	print("正在切换===",page,"页")

	input = driver.find_element_by_css_selector("#mainsrp-pager div div div div.form input")
	#清空内容（一定要清空）
	input.clear()
	#输入传入的页面
	input.send_keys(page)

	submit = driver.find_element_by_css_selector("#mainsrp-pager div div div div.form span.btn.J_Submit")
	submit.click()

	#判断是否切换成功,等待校验是否成功，
	wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,"#mainsrp-pager > div > div > div > ul > li.item.active"),str(page)))

	#解析对应页面的数据
	get_product_info(page)#得到切换好的当前页面的数据


def get_product_info(page):
	print("当前正在解析========",page,"页")

	#判断页面是否加载完成
	wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#mainsrp-itemlist .items .item")))

	#当前页面的数据
	html = driver.page_source

	soup = BeautifulSoup(html,"lxml")
	#得到当前页面的所以的商品标签item
	product_lists =  soup.select("#mainsrp-itemlist .items .item")

	for product in product_lists:
		print("---"*100)
		item = {}
		#出售地点
		location = product.select(".location")[0].text
		#店铺名称
		shopname = product.select(".shopname")[0].text
		#商品名称
		title = product.select(".title .J_ClickStat")[0].text

		#商品的图片
		iamge = product.select("img")[0]["data-src"]

		data_link = product.select(".pic-link.J_ClickStat.J_ItemPicA")[0]["href"]

		# print(location,shopname,title,iamge,data_link)
		item["location"] = location
		item["shopname"] = shopname
		item["title"] = title
		item["iamge"] = iamge
		item["data_link"] = data_link

		print(item)

#得到总页数

def get_total_page():
	#浏览器输入网站
	driver.get("https://www.taobao.com/")
	#等待搜索宽加载完成,返回控件的引用
	input = wait.until(EC.presence_of_element_located((By.ID,"q")))
	# 清除搜索框的内容
	input.clear()
	#输入美食
	input.send_keys("美食")

	#按点击按钮
	# driver.find_element_by_css_selector(".btn-search").click()
	driver.find_element_by_class_name("btn-search").click()

	#第1页

	#得到总页数,字符串  共 100 页，

	total = driver.find_element_by_class_name("total").text
	# print(total)
	total_num = re.compile(r'\d+').search(total).group()

	#写一个函数获取当前页（第一页的数据）

	get_product_info(1)



	return total_num



if __name__ == "__main__":
	toto_page = get_total_page()
	print("总页数===",toto_page)

	for page in range(2,int(toto_page)+1):
		print(page)
		next_page(page)

	#退出浏览器
	driver.quit()