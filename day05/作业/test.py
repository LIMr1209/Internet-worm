from selenium import webdriver
import time

url = "http://www.baidu.com"
driver = webdriver.Chrome()
driver.get(url)

driver.find_element_by_id("kw").send_keys("尚硅谷")
time.sleep(1)
driver.find_element_by_id("su").click()
driver.save_screenshot("尚硅谷.png")
driver.quit()
