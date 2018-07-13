# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from DongGuan.items import DongguanItem


class QuestionSpider(CrawlSpider):
    name = 'Question'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        # follow 默认是True
        Rule(LinkExtractor(allow=r'type=4')),  # 匹配下一页的规则,不写回调函数把匹配到的链接请求并送给下面这个规则
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), process_links='handler_links', callback='parse_item',
             follow=True),
    )

    # 在这个函数中可以处理得到的错误链接，在这儿得到的是正确的链接不做修改，必须返回 links
    def handler_links(self, links):
        for link in links:
            pass
            # print(link)
        return links

    def parse_item(self, response):
        # print('-------' * 100)
        item = DongguanItem()
        url = response.url
        title_num = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()

        title = title_num[0].split('\xa0\xa0')[0]
        title = title.split('：')[1]
        # print(title)
        number = title_num[0].split('\xa0\xa0')[1]
        number = number.split(':')[1]
        # print(number)
        content = response.xpath('//div[@class="c1 text14_2"]/text() | //div[@class="contentext"]/text()').extract()
        content = ''.join(content).strip()
        # print(content)
        item['url'] = url
        item['title'] = title
        item['number'] = number
        item['content'] = content
        yield item
