from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor

from scrapy_redis.spiders import RedisCrawlSpider

#MyCrawler继承RedisCrawlSpider
class MyCrawler(RedisCrawlSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    #爬虫名称
    name = 'mycrawler_redis'
    #首次向分布式爬虫发指令的
    #lpush mycrawler:start_urls url的起始位置
    redis_key = 'mycrawler:start_urls'

    #当运行爬虫的命令scrapy runspider mycrawler_redis.py

    rules = (
        # follow all links,只要是链接都匹配成功，并且帮我请求，回调parse_page
        Rule(LinkExtractor(), callback='parse_page', follow=True),
    )

    allowed_domains = ['atguigu.com']
	 #
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MyCrawler, self).__init__(*args, **kwargs)

    def parse_page(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
