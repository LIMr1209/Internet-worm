
from selenium import webdriver

#创建了一个没有界面的浏览器
driver = webdriver.PhantomJS(executable_path="/usr/bin/phantomjs")

#请求网站http://www.baidu.com
driver.get("http://www.baidu.com")

#打印百度的标题
print(driver.title)

driver.save_screenshot("百度首页.png")

#退出浏览
driver.quit()
