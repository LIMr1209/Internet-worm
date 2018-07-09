import requests
from threading import Thread, Lock
from lxml import etree
from queue import Queue
import json


crawl_switch = False
parse_switch = False


class CrawlThread(Thread):
    def __init__(self, thread_name, page_queue, data_queue):
        super(CrawlThread, self).__init__()
        self.thread_name = thread_name
        self.page_queue = page_queue
        self.data_queue = data_queue

    def run(self):
        while not crawl_switch:
            try:
                page = self.page_queue.get(block=False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                print('%s正在采集第%s页,%s' % (self.thread_name, page, url))
                response = requests.get(url)
                html = response.content
                self.data_queue.put(html)
            except Exception as e:
                pass


class ParseThread(Thread):
    def __init__(self, thread_name, data_queue, file_name, lock):
        super(ParseThread, self).__init__()
        self.thread_name = thread_name
        self.data_queue = data_queue
        self.file_name = file_name
        self.lock = lock

    def run(self):
        while not parse_switch:
            try:
                html = self.data_queue.get(block=False)
                print(self.thread_name + '开始解析数据')
                self.parse(html)
            except Exception as e:
                pass

    def parse(self, html):
        # xpath获取数据
        html = etree.HTML(html)
        # 把数据加入列表
        items = []
        # 得到所以的节点
        node_list = html.xpath('//div[contains(@id,"qiushi_tag")]')
        for node in node_list:
            # 字典
            item = {}
            items.append(item)  # 可以
            # 遍历每个节点，从节点取出用户头像，和用户，段子，点赞和评论数
            user_image = node.xpath('./div/a/img/@src')
            # 用户名
            user_name = node.xpath('./div/a/h2/text()')
            # 段子
            content = node.xpath('./a/div/span/text()')
            # 点赞
            love_num = node.xpath('./div[@class="stats"]/span/i/text()')
            # 评论
            comment = node.xpath('./div[@class="stats"]/span/a/i/text()')

            if len(user_image) > 0:
                iamge_url = user_image[0]
                item["iamge_url"] = iamge_url

            # print(iamge_url)

            if len(user_name) > 0:
                user_name = user_name[0]
                item["user_name"] = user_name
            # print(user_name)

            if len(content) > 0:
                content = "".join(content)
                item["content"] = content
            # print(content)

            if len(love_num) > 0:
                love_num = love_num[0]
                # print(love_num)
                item["love_num"] = love_num

            if len(comment) > 0:
                comment = comment[0]
                # print(comment)
                item["comment"] = comment
        with self.lock:
            json.dump(items,self.file_name,ensure_ascii=False)
            print('保存成功')



def main():
    global crawl_switch
    global parse_switch
    page_queue = Queue(10)
    data_queue = Queue()
    lock = Lock()
    for page in range(1, 11):
        page_queue.put(page)
    crawl_threads = []
    crawl_thread_name = ['采集线程1', '采集线程2', '采集线程3']
    for thread_name in crawl_thread_name:
        thread = CrawlThread(thread_name, page_queue, data_queue)
        thread.start()
        crawl_threads.append(thread)
    file_name = open('糗事百科.json', 'a')
    parse_threads = []
    parse_thread_name = ['解析线程1', '解析线程2', '解析线程3']
    for thread_name in parse_thread_name:
        thread = ParseThread(thread_name, data_queue, file_name, lock)
        thread.start()
        parse_threads.append(thread)

    while not page_queue.empty():
        pass
    crawl_switch = True
    for thread in crawl_threads:
        thread.join()
    while not data_queue.empty():
        pass
    parse_switch = True
    for thread in parse_threads:
        thread.join()
    with lock:
        file_name.close()
    print('主线程结束')



if __name__ == '__main__':
    main()
