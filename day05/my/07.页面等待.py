from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 显示等待
driver = webdriver.Chrome()

wait = WebDriverWait(driver, 5)

driver.get('http://www.taobao.com/')

input = wait.until(EC.presence_of_element_located((By.ID, 'q')))

input.send_keys('美食')

sublime = driver.find_element_by_css_selector('.search-button')

sublime.click()


# 隐式等待
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.get('http://www.taobao.com/')
#
# input = driver.find_element_by_id('q')
#
# input.send_keys('美食')
#
# sublime = driver.find_element_by_css_selector('.search-button')
#
# sublime.click()