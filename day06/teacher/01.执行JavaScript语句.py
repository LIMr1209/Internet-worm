from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "https://movie.douban.com/typerank?type_name=%E5%89%A7%E6%83%85&type=11&interval_id=100:90&action="

driver.get(url)
driver.save_screenshot("变化之前.png")

time.sleep(3)

print(driver.page_source)

print(driver.title)
var = "var q=document.getElementById(\"db-nav-movie\");q.style.border=\"1px solid red\";"

driver.execute_script(var)

time.sleep(3)
driver.save_screenshot("变化之后.png")