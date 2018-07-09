# import time
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# #创建了一个谷歌浏览器的浏览器
#
# driver = webdriver.Chrome()
# driver.get("http://www.gulixueyuan.com/register?goto=/")
# # 打印页面标题 "百度一下，你就知道
#
# data = driver.find_element_by_name("verifiedMobile")
# #data = driver.find_element(by=By.ID,value="login")
# print(data.get_attribute("placeholder"))
# #得到内容
# print(data.tag_name)


import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
#创建了一个谷歌浏览器的浏览器

driver = webdriver.Chrome()
driver.get("http://192.168.28.49:8080/index.html")
# 打印页面标题 "百度一下，你就知道

select = Select(driver.find_element_by_id("status"))
#根据下标去选择
# select.select_by_index(3)

select.select_by_value("3")
