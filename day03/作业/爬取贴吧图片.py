import requests
from lxml import etree
import os

def save_image(result):
    response = requests.get(result)
    if not os.path.exists('images'):
        os.makedirs('images')
    image_file_name = result[len(result)-10:]
    with open('images/'+image_file_name,'wb') as f:
        f.write(response.content)
    print('保存成功', image_file_name)

def get_image_url(tieba_detail_url):
    response = requests.get(tieba_detail_url)
    html_obj = etree.HTML(response.content.decode())
    result_list = html_obj.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
    for result in result_list:
        save_image(result)


def tieba_spider(kw, url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        page = (page - 1) * 50
        params = {
            'pn': str(page),
            'kw': kw
        }
        # headers = {
        #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
        # }
        response = requests.get(url, params=params)
        html = response.content.decode()
        print(response.url)
        html_obj = etree.HTML(html)
        result_list = html_obj.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
        for result in result_list:
            tieba_detail_url = "https://tieba.baidu.com" + result
            get_image_url(tieba_detail_url)

def main():
    kw = input("请输入您要爬取贴吧名称：")
    start_page = int(input("请输入您要爬取起始页面:"))
    end_page = int(input("请输入您要爬取结束页面:"))
    url = "https://tieba.baidu.com/f?" + "&ie=utf-8"
    tieba_spider(kw, url, start_page, end_page)


if __name__ == '__main__':
    main()
