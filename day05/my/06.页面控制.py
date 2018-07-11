# find_element_by_id  根据标签id选单个标签
# find_elements_by_name  根据标签name属性值选多个标签  一个列表
# find_element_by_name  根据标签name属性值选一个标签
# find_elements_by_xpath  根据xpath选多个标签  一个列表
# find_element_by_xpath  根据xpath选一个标签
# from selenium.webdriver.common.by import By
# inputs = driver.find_elements(By.XPATH, "//input")  根据xpath选多个标签



#获取内容为cheese的标签
# cheese = driver.find_element_by_link_text("cheese")
# ------------------------ or -------------------------
# from selenium.webdriver.common.by import By
# cheese = driver.find_element(By.LINK_TEXT, "cheese")



# find_elements_by_partial_link_text

# find_elements_by_class_name   根据标签的class类名获取斗个标签
# find_elements_by_css_selector    #根据css选择器选取多个标签
# find_elements_by_tag_name("input")  根据标签名选多个标签 一个列表


# elements 是选取多个且为列表    element  获取一个
