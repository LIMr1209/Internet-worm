from selenium import webdriver

# 调用环境变量指定的PhantomJS浏览器创建浏览器对象
# 如果没有在环境变量指定PhantomJS位置


# PhantomJS  过时
driver = webdriver.PhantomJS(
    executable_path="C:/Users/ST/AppData/Local/Programs/Python/Python36/Scripts/phantomjs-2.1.1-windows/bin/phantomjs.exe")

# get方法会一直等到页面被完全加载，然后才会继续程序，通常测试会在这里选择
driver.get("http://www.baidu.com/")
# 打印页面标题 "百度一下，你就知道
print(driver.title)

# 生成当前页面快照并保存
driver.save_screenshot("baidu.png")
# 关闭浏览器
driver.quit()
