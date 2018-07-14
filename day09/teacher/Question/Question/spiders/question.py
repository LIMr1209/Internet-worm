# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from Question.items import QuestionItem

class QuestionSpider(CrawlSpider):
    name = 'question'
    allowed_domains = ['wz.sun0769.com']
    pre='http://wz.sun0769.com/index.php/question/questionType?type=4&page='
    offset=0
    start_urls = [pre+str(offset)]

    rules = (
        Rule(LinkExtractor(allow=r'type=4'), follow=True),
        Rule(LinkExtractor(allow=r'/question/\d+/\d+.shtml'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = QuestionItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()
        link=response.url
        titles=response.xpath('//div[@class="pagecenter p3"]//strong[@class="tgray14"]/text()').get()
        title=titles.strip()[4:-10]
        num=titles.strip()[-6:]
        content=response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        item['link']=link
        item['title'] = title
        item['num'] = num
        item['content'] = "".join(content).strip()
        return item
