from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re

options = Options()
options.add_argument('--headless')
SERVICE_ARGS = ['--load-images=false', '--disk-cache=false']
driver = webdriver.Chrome(options=options,service_args=SERVICE_ARGS)
wait = WebDriverWait(driver, 5)


def next_page(page):
    print('正在翻页---------',page)
    input = driver.find_element_by_css_selector('.form input')
    input.clear()
    input.send_keys(page)
    submit = driver.find_element_by_css_selector('.form .J_Submit')
    submit.click()
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'li.item.active'),str(page)))
    get_product_info()


def get_page_num():
    url = 'http://www.taobao.com/'
    driver.get(url)
    input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
    input.send_keys('美食')
    submit = driver.find_element_by_class_name('btn-search')
    submit.click()
    total_page_num = driver.find_element_by_class_name('total').text
    page_num = re.compile(r'\d+').search(total_page_num).group()
    get_product_info()
    return page_num


def get_product_info():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .item')))
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    items = soup.select('#mainsrp-itemlist .item')
    for item in items:
        item_dict = {}
        shop_name = item.select('.title')[0].get_text().strip()
        price = item.select('.price')[0].get_text().strip()
        location = item.select('.location')[0].get_text().strip()
        image = item.select('img')[0]['data-src']
        shop_link = item.select('.pic a')[0]['href']
        print(image, shop_link)
        item_dict['shop_name'] = shop_name
        item_dict['price'] = price
        item_dict['image'] = image
        item_dict['location'] = location
        item_dict['shop_link'] = shop_link
        print(item_dict)


if __name__ == '__main__':
    page_num = get_page_num()
    for i in range(2, int(page_num) + 1):
        next_page(i)
