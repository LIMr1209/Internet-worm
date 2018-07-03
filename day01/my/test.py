from urllib.request import Request, urlopen
from urllib import parse


def save_html(file_name, html):
    print('正在保存', file_name)
    with open(file_name, 'wb') as f:
        f.write(html)
    print('保存成功', file_name)


def down_page(full_url):
    print('正在下载,', full_url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"
    }
    request = Request(full_url, headers=headers)
    response = urlopen(request)
    return response.read()


def baidu_spider(url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        pn = (page - 1) * 50
        full_url = url + '&pn=' + str(pn)
        html = down_page(full_url)
        file_name = '第' + str(page) + '页.html'
        save_html(file_name, html)


def main():
    kw = input('请输入贴吧名:')
    start_page = int(input('开始页码:'))
    end_page = int(input('结束页码:'))
    kw = {'kw': kw}
    kw = parse.urlencode(kw)
    # url = 'https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B7&ie=utf-8&pn=200'
    url = 'https://tieba.baidu.com/f?' + kw
    baidu_spider(url, start_page, end_page)


if __name__ == '__main__':
    main()
