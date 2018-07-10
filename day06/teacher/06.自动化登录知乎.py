import time
from selenium import webdriver
import base64
from PIL import Image
from pytesseract import image_to_string


def get_image_text():
    reuslt_text = None
    try:
        image = Image.open("captcha.jpg")
        reuslt_text = image_to_string(image)
        print("reuslt_text:", reuslt_text)
    except Exception as e:
        print(e)

    if reuslt_text == None:
        reuslt_text = input("请输入验证码：")

    return reuslt_text


# 保存验证码
def save_captcha(base64data):
    base64data = base64data[len("data:image/jpg;base64,"):].replace("&#10;", "").replace("%0A", "")
    print("image_data==", base64data)
    image_data = base64.b64decode(base64data)

    with open("captcha.jpg", "wb") as file:
        file.write(image_data)

    print("验证保存成功！")


def zhihulogin():
    driver = webdriver.Chrome()
    # 进入登录页面
    driver.get("https://www.zhihu.com/signup?next=%2F")
    time.sleep(2)
    # 点击切换到登录页面
    driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span').click()

    # 输入账号
    driver.find_element_by_name("username").send_keys("trygf521@126.com")

    # 输入密码
    driver.find_element_by_name("password").send_keys("afu123456")
    driver.save_screenshot("输入账号和密码完毕.png")

    if driver.page_source.find("Captcha-englishContainer") != -1:
        src = driver.find_element_by_class_name("Captcha-englishImg").get_attribute("src")
        print(src)

        if len(src) > len("data:image/jpg;base64,null"):
            # 英文验证码出现
            print("英文验证码出现")
            save_captcha(src)

            # 识别验证码
            reuslt_text = get_image_text()
            input = driver.find_element_by_xpath('//div[@class="Input-wrapper"]/input')
            input.send_keys(reuslt_text)

        else:
            print("没有英文验证码")



    elif driver.page_source.find("Captcha-chineseContainer") != 1:
        src = driver.find_element_by_class_name("Captcha-chineseImg").get_attribute("src")
        print(src)

        if len(src) > len("data:image/jpg;base64,null"):
            # 中文验证码出现
            print("出现中文验证码了")
            save_captcha(src)
            # 退出浏览器
            driver.quit()

        else:
            print("没有中文验证码")

    # 判断英文和中文验证处理

    sibmit = driver.find_element_by_xpath('//div[@class="Login-content"]/form/button')

    # 点击登录
    sibmit.click()
    time.sleep(5)

    # 保存登录成功的照片
    driver.save_screenshot("登录成功.png")


if __name__ == "__main__":
    zhihulogin()
