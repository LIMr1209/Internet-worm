# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider

from python_job.items import PythonJobItem


class Job4Spider(RedisCrawlSpider):
    name = 'job4'
    allowed_domains = ['51job.com']
    #lpush job4spider:start_urls https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
    redis_key = 'job4spider:start_urls'

    rules = (
        Rule(LinkExtractor(allow=r'python,2,\d+.html/')),
        Rule(LinkExtractor(allow=r'com/.+/\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = PythonJobItem()
        print("response.url==", response.url)
        title = response.xpath('//div[@class="cn"]/h1/text()').extract()
        title = "".join(title)

        location = response.xpath('//div[@class="cn"]/span/text()').extract()
        location = "".join(location)
        salary = response.xpath('//div[@class="cn"]/strong/text()').extract()

        salary = "".join(salary)
        company_name = response.xpath('//div[@class="cn"]/p/a/text()').extract()
        company_name = "".join(company_name)
        company_info = response.xpath('//div[@class="cn"]/p[@class="msg ltype"]/text()').extract()
        company_info = "".join(company_info).strip()
        experience = response.xpath('//div[@class="t1"]/span[1]/text()').extract()
        experience = "".join(experience).strip()
        job_info = response.xpath(
            '//div[@class="bmsg job_msg inbox"]/p/text()|//div[@class="bmsg job_msg inbox"]/text()|//div[@class="bmsg job_msg inbox"]//p//span/text()').extract()
        job_info = "".join(job_info).strip()
        address = response.xpath('//div[@class="bmsg inbox"]/p/text()').extract()

        address = "".join(address).strip()
        item["url"] = response.url

        item["title"] = title
        item["location"] = location

        item["salary"] = salary

        item["company_name"] = company_name

        item["company_info"] = company_info

        item["experience"] = experience

        item["job_info"] = job_info

        item["address"] = address
        yield item
