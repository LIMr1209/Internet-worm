from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")
# 打印页面标题 "百度一下，你就知道
# print(driver.title)
driver.find_element_by_id('kw').send_keys('女优')  # 找到百度输入框，输入内容
driver.find_element_by_id('su').click()  # 找到百度一下点击按钮，并点击
# 生成当前页面快照并保存
time.sleep(2)
print(driver.page_source)  # 页面源代码
# print(driver.get_cookies())  # cookies 信息
# print(driver.current_url)  #网页网址
driver.save_screenshot("baidu.png")  # 截屏
time.sleep(5)
# ctrl + a 全选
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
time.sleep(5)
# ctrl + x 剪切
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

# 关闭浏览器
