from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

#sccrapy规则爬虫
from example.items import ExampleItem


class DmozSpider(CrawlSpider):
    """Follow categories and extract links."""
    name = 'chinadmoz'
    allowed_domains = ['chinadmoz.org']
    start_urls = ['http://www.chinadmoz.org/']

    rules = [
        Rule(LinkExtractor(allow=r"/subindustry/\d+/"), callback='parse_directory', follow=True),
    ]

    def parse_directory(self, response):

        node_all = response.xpath('//ul[@class="boxbdnopd"]/li')

        for node in node_all:
            item = ExampleItem()
            name = node.xpath('.//h4/a/text()').extract()[0]

            link = node.xpath('.//h4/a/@href').extract()[0]

            description = node.xpath('.//p[@class="description"]/text()').extract()[0]

            item["name"] = name
            item["link"] = link
            item["description"] = description

            print("link==",link)
            yield item


        # for div in response.css('.title-and-desc'):
        #     yield {
        #         'name': div.css('.site-title::text').extract_first(),
        #         'description': div.css('.site-descr::text').extract_first().strip(),
        #         'link': div.css('a::attr(href)').extract_first(),
        #     }
