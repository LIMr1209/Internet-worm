from selenium import webdriver
import time
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
    return reuslt_text


def save_captcha(captcha):
    data = captcha[len("data:image/jpg;base64,"):].replace('&#10', '').replace("%0A", '')
    image_data = base64.b64decode(data)
    with open("captcha.jpg", "wb") as f:
        f.write(image_data)

    print("验证保存成功！")


def main():
    url = 'https://www.zhihu.com/signup?next=%2F'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_xpath('//div[@class="SignContainer-switch"]/span').click()
    driver.find_element_by_name('username').send_keys('trygf521@126.com')
    driver.find_element_by_name('password').send_keys('afu123456')
    driver.save_screenshot('输入账号密码.png')
    if driver.page_source.find('Captcha-chineseContainer') != -1:
        src = driver.find_element_by_class_name('Captcha-chineseImg').get_attribute('src')
        if len(src) > len('data:image/jpg;base64,null'):
            print('中文验证码出现')
            save_captcha(src)
            driver.quit()
        else:
            print('没有中文验证码')
    elif driver.page_source.find('Captcha-englishContainer') != -1:
        src = driver.find_element_by_class_name('Captcha-englishImg').get_attribute('src')
        if len(src) > len('data:image/jpg;base64,null'):
            print('英文验证码出现')
            save_captcha(src)
            result_text = get_image_text()
            a = driver.find_element_by_xpath('//div[@class="Input-wrapper"]/input')
            a.send_keys(result_text)
        else:
            print('没有英文验证码')
    submit = driver.find_element_by_xpath('//div[@class="Login-content"]/form/button')

    # 点击登录
    submit.click()

    while True:
        if driver.find_element_by_class_name('Captcha-errorMessage').text:
            result_text = input('输入验证码')

            a = driver.find_element_by_xpath('//div[@class="Input-wrapper"]/input')
            a.send_keys(result_text)
            submit = driver.find_element_by_xpath('//div[@class="Login-content"]/form/button')

            # 点击登录
            submit.click()
        break
    # 保存登录成功的照片
    time.sleep(5)
    driver.save_screenshot("登录成功.png")


if __name__ == '__main__':
    main()
