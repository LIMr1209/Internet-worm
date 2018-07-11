from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.douban.com/")
time.sleep(3)
driver.save_screenshot('豆瓣登录页面.png')

driver.find_element_by_id('form_email').send_keys('trygf521@126.com')

driver.find_element_by_id('form_password').send_keys('afu123456')

driver.save_screenshot('验证码.png')

check_code = input('输入验证码')

driver.find_element_by_id('captcha_field').send_keys(check_code)

driver.find_element_by_xpath('//input[@class="bn-submit"]').click()

time.sleep(3)

driver.save_screenshot('登录成功.png')

with open('豆瓣.html','w',encoding='utf-8') as f:
    f.write(driver.page_source)