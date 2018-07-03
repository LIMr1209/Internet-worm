from urllib.request import Request, urlopen
from urllib import parse


def save_html(filename, html):
    print('正在保存', filename)
    with open(filename, 'wb') as f:
        f.write(html)
    print('保存成功', filename)


def down_html(full_url):
    headers = {
        'User-Agent': ''
    }
    request = Request(full_url, headers=headers)
    # request.add_header('User-Agent','')
    response = urlopen(request)
    # print(request.get_full_url())
    # print(request.get_header('User-agent'))
    # print(response.info())
    return response.read()


def baidu_spider(url, start_page, end_page):
    for page in range(start_page, end_page + 1):
        pn = (page - 1) * 50
        full_url = url + '&pn=' + str(pn)
        filename = '第' + str(page) + '页.html'
        print(full_url)
        print('开始下载', full_url)
        html = down_html(full_url)
        save_html(filename, html)


def main():
    kw = input('请输入贴吧名:')
    start_page = int(input('开始页数:'))
    end_page = int(input('结束页数:'))
    kw = {'kw': kw}
    kw = parse.urlencode(kw)
    # url = 'https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B7&pn=50'
    url = 'https://tieba.baidu.com/f?' + kw
    baidu_spider(url, start_page, end_page)


if __name__ == '__main__':
    main()




