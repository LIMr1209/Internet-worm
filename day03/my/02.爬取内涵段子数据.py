from urllib.request import Request, urlopen
import re


class Spider(object):
    def save_page(self, item):
        with open('内涵段子.txt', 'a') as f:
            f.write(item)

    def print_page(self, item_list, page):
        print('正在打印第' + str(page) + "页的段子")
        for item in item_list:
            item = item.replace('&ldquo;', '"').replace('&rdquo;', '"').replace('<div class="f18 mb20">', '').replace(
                '</div>', '').replace('<p>', '').replace('</p>', '').replace('<br />', '').replace('&hellip;', '')
            print(item)
            self.save_page(item)
        print('保存第' + str(page) + '页成功')

    def load_page(self, page):
        print('正在下载第' + str(page) + '页')
        url = 'http://www.neihanpa.com/article/list_5_' + str(page) + '.html'
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36"}
        request = Request(url, headers=headers)
        response = urlopen(request)
        return response.read()

    def start(self):
        print('开始爬取')
        self.page = 1
        content = self.load_page(self.page).decode('gbk')
        pattern = re.compile('<div class="f18 mb20">.*?</div>', re.S)
        item_list = pattern.findall(content)
        self.print_page(item_list, self.page)
        while True:
            switch = input('是否继续爬取下一页')
            if switch == 'yes':
                self.page += 1
                content = self.load_page(self.page).decode('gbk')
                pattern = re.compile('<div class="f18 mb20">.*?</div>', re.S)
                item_list = pattern.findall(content)
                self.print_page(item_list, self.page)
            elif switch == 'no':
                break


if __name__ == '__main__':
    spider = Spider()
    spider.start()
