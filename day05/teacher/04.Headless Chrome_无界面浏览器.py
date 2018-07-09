import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#配置谷歌浏览器变成无界面的浏览器
options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

driver.get("http://www.baidu.com")

#得到标题
print(driver.title)
#和requests请求的数据一样


driver.save_screenshot("百度首页")


driver.find_element_by_id("kw").send_keys("尚硅谷")

#点击确定
driver.find_element_by_id("su").click()
time.sleep(3)

print(driver.page_source)
