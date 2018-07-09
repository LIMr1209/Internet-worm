import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#创建了一个谷歌浏览器的浏览器


driver = webdriver.Chrome()

#请求网站http://www.baidu.com
driver.get("http://www.baidu.com")

#打印百度的标题
print(driver.title)

driver.save_screenshot("百度首页.png")

#得到id为kw元素，向里面输入内容“女神”
driver.find_element_by_id("kw").send_keys("女神")
time.sleep(2)

#找到百度一些按钮，点击
driver.find_element_by_id("su").click()

time.sleep(2)

driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"a")

time.sleep(2)
driver.find_element_by_id("kw").send_keys(Keys.CONTROL,"x")

time.sleep(5)

driver.find_element_by_id("kw").send_keys("男神")
time.sleep(2)
#找到百度一些按钮，点击
su = driver.find_element_by_id("su")
#得到按钮的文字
print(su.get_attribute("value"))
#点击按钮
su.click()
time.sleep(5)
#退出浏览
driver.quit()
