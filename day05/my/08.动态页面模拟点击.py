from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import time


def douyu():
    # 统计多少页
    page = 1
    # 统计有多少个主播，主题
    num_total = 0

    options = Options()
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)

    driver.get("https://www.douyu.com/directory/all")

    while True:

        print('当前爬取的页面是==========================================================', page)

        data = driver.page_source
        #
        # soup = BeautifulSoup(data, "lxml")
        # print(data)
        # 得到当前页面的直播主题
        names = driver.find_elements_by_css_selector(".ellipsis")

        # names = soup.find_all("h3", attrs={"class": "ellipsis"})
        # names = soup.select('h3[class="ellipsis"]')

        # 观看人数
        # numbers = driver.find_elements_by_css_selector("span.dy-num")
        numbers = driver.find_elements_by_css_selector("span.dy-num.fr")
        # numbers = soup.find_all("span", {"class": "dy-num fr"})
        # numbers = soup.select('span[class="dy-num fr"]')

        name_numbers = zip(names, numbers)

        for name, number in name_numbers:
            # 直播主题
            title = name.text.strip()
            # 观看人数
            number = number.text.strip()
            print("直播主题===", title, "观看人数===", number)
            num_total += 1

        # 是否要点击下一页

        if data.find("shark-pager-disable-next") != -1:
            # 是最后一页
            break
        else:
            # 不是最后一页
            time.sleep(0.1)
            try:

                driver.find_element_by_class_name("shark-pager-next").click()
            except Exception as e:
                print(e)
                continue  # 如果出现异常了，页面不往下加

            page += 1

    print("当前主播人数：", num_total, "共计：", page, "页")


if __name__ == "__main__":
    douyu()
