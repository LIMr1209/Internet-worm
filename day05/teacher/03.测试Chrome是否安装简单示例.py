import time
from selenium import webdriver

#创建了一个谷歌浏览器的浏览器
driver = webdriver.Chrome()

#请求网站http://www.baidu.com
driver.get("http://www.baidu.com")

#打印百度的标题
print(driver.title)

driver.save_screenshot("百度首页.png")

#得到id为kw元素，向里面输入内容“女神”
driver.find_element_by_id("kw").send_keys("女神")

#找到百度一些按钮，点击
driver.find_element_by_id("su").click()

time.sleep(5)

#退出浏览
driver.quit()
