import requests
import re


def save_result(result):
    with open('内涵段子.txt', 'a') as f:
        f.write(result)


def print_page(result_list, page):
    print('正在打印第' + str(page) + "页的段子")
    for result in result_list:
        result = result.replace('&ldquo;', '"').replace('&rdquo;', '"').replace('<div class="f18 mb20">', '').replace(
            '</div>', '').replace('<p>', '').replace('</p>', '').replace('<br />', '').replace('&hellip;', '')
        print(result)
        save_result(result)
    print('保存第' + str(page) + '页成功')


def load_page(page):
    print('正在下载第' + str(page) + '页')
    url = 'http://www.neihanpa.com/article/list_5_' + str(page) + '.html'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
    response = requests.get(url, headers=headers)
    return response.content.decode('gbk')


def main():
    print('开始爬取')
    page = 1
    pattern = re.compile(r'<div class="f18 mb20">.*?</div>',re.S)
    html = load_page(page)
    result_list = pattern.findall(html)
    # print(result_list)
    print_page(result_list, page)
    while True:
        switch = int(input('是否继续保存下一页,0退出,1继续'))
        if switch:
            page += 1
            html = load_page(page)
            result_list = pattern.findall(html)
            print_page(result_list, page)
        else:
            break


if __name__ == '__main__':
    main()
