# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from python_job.items import PythonJobItem


class Job3Spider(RedisSpider):
    name = 'job3'
    allowed_domains = ['51job.com']
    #lpush job3spider:start_urls https://search.51job.com/list/010000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=
    redis_key = 'job3spider:start_urls'

    def parse(self, response):
        links = response.xpath('//div[@class="el"]/p//a/@href').extract()
        for link in links:
            yield scrapy.Request(link, callback=self.parse_detail)

        next_url = response.xpath('//li[@class="bk"][last()]/a/@href').extract()
        if next_url:
            next_url = next_url[0]
            yield scrapy.Request(next_url, callback=self.parse)
        else:
            print('已爬完')

    def parse_detail(self, response):
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
