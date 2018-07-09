from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time
import unittest

options = Options()
options.add_argument('--headless')


class MyTest(unittest.TestCase):
    def setUp(self):
        print('开始测试')

    def testMain(self):
        page = 1
        num_total = 0
        while True:
            driver = webdriver.Chrome(options=options)
            driver.get("https://www.douyu.com/directory/all")
            print('当前爬取的页面为-------', str(page))
            names = driver.find_elements_by_css_selector('.ellipsis')
            nums = driver.find_elements_by_css_selector('span.dy-num.fr')
            html = driver.page_source
            #
            # soup = BeautifulSoup(html,'lxml')
            # names = soup.find_all('h3',attrs={'class':'ellipsis'})
            # names = soup.select('h3[class="ellipsis"]')
            # nums = soup.find_all('span',attrs={'class':'dy-num fr'})
            # nums = soup.select('span[class="dy-num fr"]')
            item = zip(names, nums)
            for name, num in item:
                # print(name.get_text())
                title = name.text.strip()
                number = num.text.strip()
                num_total += 1
                print("直播主题===", title, "观看人数===", number)
            if html.find("shark-pager-disable-next") != -1:
                break
            else:
                # 不是最后一页
                time.sleep(0.1)
                try:

                    driver.find_element_by_class_name("shark-pager-next").click()
                except Exception as e:
                    continue  # 如果出现异常了，页面不往下加

                page += 1

        print("当前主播人数：", num_total, "共计：", page, "页")

    def tearDown(self):
        print('测试结束')


if __name__ == '__main__':
    unittest.main()
