from urllib import parse
from urllib.request import Request, urlopen

from lxml import etree
import os


def save_page(filename, data):
    print("正在保存：", filename)
    with open(filename, 'wb') as f:
        f.write(data)

    print("保存完毕：", filename)


def save_image(image_url):
    request = Request(image_url)
    response = urlopen(request)
    data = response.read()  # bytes类型

    # 如果./images不存在就创建
    if not os.path.exists("./images/"):
        os.makedirs("./images/")
    image_name = image_url[len(image_url) - 10:]
    print("图片名称==", image_name)
    with open("./images/" + image_name, "wb") as f:
        f.write(data)


def download_page(full_url):
    print("正在下载==", full_url)
    # headers = {
    # 	"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    # }
    request = Request(full_url)

    response = urlopen(request)

    return response.read()  # bytes类型


def get_image_url(tieba_url):
    request = Request(tieba_url)

    response = urlopen(request)

    html = response.read().decode()
    # print(html)
    # 得到图片的链接
    result = etree.HTML(html)
    # 图片列表
    list_image_href = result.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src')
    print(list_image_href)
    for image_url in list_image_href:
        # 保存图片
        save_image(image_url)


# 拼接页面函数
def baidu_spider(url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        # print(page)
        # page:当前页，mysql,分页（n-1）*m,m,n页码，m每页多少条数据
        pn = (page - 1) * 50  # int

        ## url = "https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B7&ie=utf-8&pn=50"
        full_url = url + "&pn=" + str(pn)
        print(full_url)
        # 请求路径
        html = download_page(full_url).decode()  # bytes类型

        # print(html)

        # 得到帖子链接
        result = etree.HTML(html)
        list_href = result.xpath('//div[@class="threadlist_title pull_left j_th_tit "]/a/@href')
        # print("list_href==",list_href)

        for href in list_href:
            tieba_url = "https://tieba.baidu.com" + href
            print(tieba_url)
            get_image_url(tieba_url)

    # 请求这个帖子具体的内容，并且从内容里面得到图片

    # print("type===",type(html))
    # #文件名称
    # filename = "第"+str(page)+"页.html"
    # #保存请求到的数据
    # save_page(filename,html)


def main():
    # kw = input("请输入您要爬取贴吧名称：")#字符串
    kw = "图片"
    start_page = int(input("请输入您要爬取起始页面:"))
    end_page = int(input("请输入您要爬取结束页面:"))

    kw = {"kw": kw}  # 字典

    kw = parse.urlencode(kw)  # kw=%E5%B0%9A%E7%A1%85%E8%B0%B7

    # url = "https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B7&ie=utf-8&pn=50"

    url = "https://tieba.baidu.com/f?" + kw + "&ie=utf-8"
    print(url)
    baidu_spider(url, start_page, end_page)


if __name__ == "__main__":
    main()
