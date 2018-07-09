from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')

driver = webdriver.Chrome(options=options)
driver.get('http://www.baidu.com')
driver.find_element_by_id('kw').send_keys('女友')
driver.find_element_by_id('su').click()
time.sleep(10)
print(driver.page_source)
print(driver.current_url)
print(driver.get_cookies())
driver.save_screenshot('女友.png')

driver.quit()
