# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from Dongguan.items import DongguanItem


class QuestionSpider(CrawlSpider):
    name = 'Question'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/questionType?type=4&page=0']

    rules = (
        #Rule规则里面如果没有写Rule,默认是深度爬取
        #所以帖子的页面的数据
        Rule(LinkExtractor(allow=r'type=4'),follow=True),#下一页的匹配
        Rule(LinkExtractor(allow=r'question/\d+/\d+.shtml'), process_links="handle_links",callback='parse_item', follow=True),
    )

    #把有错误的链接，可以修改过来，再去请求
    def handle_links(self,links):
        for link in links:
            print("link====",link)

        return links

    #帖子的详细信息
    def parse_item(self, response):
        # print("response.url==",response.url)

        item = DongguanItem()

        #帖子链接
        url = response.url

        title_number = response.xpath('//div[@class="pagecenter p3"]/div/div/div/strong/text()').extract()

        if len(title_number)  > 0:
            title_number = title_number[0]
            #编号:191166
            #帖子的编号
            number = title_number.split("\xa0\xa0")[1]
            number = number.split(":")[1]

            #帖子标题
            title = title_number.split("\xa0\xa0")[0]
            title = title.split("：")[1]

            item["title"] = title
            item["number"] = number

        content = response.xpath('//div[@class="c1 text14_2"]/text()|//div[@class="contentext"]/text()').extract()
        #把列表使用“”链接变成字符串
        content = "".join(content).strip()


        # print(content)

        item["url"] = url
        item["content"] = content

        yield item



        #


