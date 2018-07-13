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
        Rule(LinkExtractor(allow=r'type=4&page=')),
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = DongguanItem()
        url = response.url
        title_num = response.xpath('//div[@class="pagecenter p3"]//strong/text()').extract()[0]
        title = title_num.split('  ')[0]
        title = title.split('：')[1]
        num = title_num.split('  ')[1]
        num = num.split(':')[1]
        content = response.xpath(
            '//div[@class="content text14_2"]/div[@class="c1 text14_2"]/text() | //div[@class="contentext"]/text()').extract()
        content = ''.join(content).strip()
        item['url'] = url
        item['title'] = title
        item['num'] = num
        item['content'] = content
        yield item
