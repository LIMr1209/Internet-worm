from queue import Queue
from threading import Thread, Lock
import requests
from lxml import etree
import json

crawl_exit = False
parse_exit = False


class ThreadCrawl(Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(ThreadCrawl, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue
        self.headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/6.0)"}

    def run(self):
        while not crawl_exit:
            try:
                page = self.page_queue.get(block=False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                print('%s开始采集第%s页,url为 %s' % (self.thread_name, page, url))
                response = requests.get(url, headers=self.headers)
                html = response.text
                self.data_queue.put(html)
            except:
                pass


class ThreadParse(Thread):
    def __init__(self, thread_name, data_queue, file_name, lock):
        super(ThreadParse, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.file_name = file_name
        self.lock = lock

    def parse(self, html):

        html = etree.HTML(html)
        items = []
        node_list = html.xpath('//div[contains(@id,"qiushi_tag")]')
        for node in node_list:
            item = {}
            items.append(item)
            user_image = node.xpath('./div/a/img/@src')
            user_name = node.xpath('./div/a/h2/text()')
            content = node.xpath('./a/div/span/text()')
            dianzhan = node.xpath('./div[@class="stats"]/span/i/text()')
            commont = node.xpath('./div[@class="stats"]/span/a/i/text()')

            if len(user_image) > 0:
                iamge_url = user_image[0]
                item["iamge_url"] = iamge_url

            if len(user_name) > 0:
                user_name = user_name[0]
                item["user_name"] = user_name

            if len(content) > 0:
                content = "".join(content)
                # print(content)
                item["content"] = content

            if len(dianzhan) > 0:
                dianzhan = dianzhan[0]
                item["dianzhan"] = dianzhan

            if len(commont) > 0:
                commont = commont[0]
                item["commont"] = commont

        with self.lock:
            json.dump(items, self.file_name, ensure_ascii=False)

    def run(self):
        while not parse_exit:
            try:
                html = self.data_queue.get(block=False)
                print(self.thread_name + "开始解析数据")
                self.parse(html)
            except:
                pass


def main():
    global crawl_exit
    global parse_exit
    page_queue = Queue(10)
    data_queue = Queue()
    lock = Lock()
    for i in range(1, 11):
        page_queue.put(i)
    crawl_thread_names = ['采集线程1', '采集线程2', '采集线程3']
    crawl_threads = []
    for thread_name in crawl_thread_names:
        thread = ThreadCrawl(thread_name, page_queue, data_queue)
        thread.start()
        crawl_threads.append(thread)
    parse_thread_names = ['解析线程1', '解析线程2', '解析线程3']
    parse_threads = []
    file_name = open('糗事百科.json', 'w', encoding='utf-8')
    for thread_name in parse_thread_names:
        thread = ThreadParse(thread_name, data_queue, file_name, lock)
        thread.start()
        parse_threads.append(thread)

    while not page_queue.empty():
        pass
    crawl_exit = True
    for thread in crawl_threads:
        thread.join()
    while not data_queue.empty():
        pass
    parse_exit = True
    for thread in parse_threads:
        thread.join()

    with lock:
        file_name.close()
        print('保存成功')


if __name__ == '__main__':
    main()
