from urllib.request import Request, urlopen
from urllib import parse
from lxml import etree
import os

def save_image(result):
    request = Request(result)
    response = urlopen(request)
    if not os.path.exists('images'):
        os.makedirs('images')
    image_file_name = result[len(result)-10:]
    with open('images/'+image_file_name,'wb') as f:
        f.write(response.read())
    print('保存成功',image_file_name)


def get_image_url(tieba_detail_url):
    request = Request(tieba_detail_url)
    response = urlopen(request)
    html_obj = etree.HTML(response.read().decode())
    result_list = html_obj.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
    for result in result_list:
        save_image(result)


def down_page(full_url):
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    # }
    request = Request(full_url)
    response = urlopen(request)
    return response.read().decode()


def tieba_spider(url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        print('爬取第' + str(page) + '页的html')
        pn = (page - 1) * 50
        full_url = url + '&pn=' + str(pn)
        print(full_url)
        html = down_page(full_url)
        html_obj = etree.HTML(html)
        result_list = html_obj.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')

        for result in result_list:
            tieba_detail_url = "https://tieba.baidu.com" + result
            get_image_url(tieba_detail_url)

def main():
    kw = input("请输入您要爬取贴吧名称：")
    start_page = int(input("请输入您要爬取起始页面:"))
    end_page = int(input("请输入您要爬取结束页面:"))
    kw = {'kw': kw}
    kw = parse.urlencode(kw)
    url = "https://tieba.baidu.com/f?" + kw + "&ie=utf-8"
    tieba_spider(url, start_page, end_page)


if __name__ == '__main__':
    main()
