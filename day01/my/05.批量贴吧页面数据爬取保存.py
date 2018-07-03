from urllib import parse
from urllib.request import Request, urlopen


def save_html(file_name, data):
    print('正在保存',file_name)
    with open(file_name, 'wb') as f:
        f.write(data)
    print('保存成功', file_name)


def baidu_stiffer(start_page, end_page, url):
    for page in range(start_page, end_page + 1):
        pn = (page - 1) * 50
        full_url = url + '&pn=' + str(pn)
        print(full_url)
        file_name = '第' + str(page) + '页.html'
        print('开始爬取第' + str(page) + '页', file_name)
        header = {
            "User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
        }
        request = Request(full_url, headers=header)
        response = urlopen(request)
        data = response.read()
        save_html(file_name, data)


def main():
    kw = input('贴吧名：')
    start_page = int(input('起始页：'))
    end_page = int(input('结束页：'))
    kw = {'kw': kw}
    kw = parse.urlencode(kw)
    # url = 'https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B7&ie=utf-8&pn=200'
    url = 'https://tieba.baidu.com/f?' + kw
    baidu_stiffer(start_page, end_page, url)


if __name__ == '__main__':
    main()
