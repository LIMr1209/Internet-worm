from selenium import webdriver
import time
from selenium.webdriver.chrome.options import  Options

options = Options()
options.add_argument("--headless")


driver = webdriver.Chrome(options=options)

driver.get("https://www.douban.com/")

# time.sleep(2)

driver.save_screenshot("豆瓣登录.png")

#输入账号和密码
driver.find_element_by_id("form_email").send_keys("trygf521@126.com")

#输入密码
driver.find_element_by_name("form_password").send_keys("afu123456")

#点击登录按钮
driver.find_element_by_xpath('//input[@class="bn-submit"]').click()

driver.save_screenshot("豆瓣登录成功.png")

#成功后保存页面
with open("豆瓣网.html","w") as f:
	print(driver.page_source)
	f.write(driver.page_source)
