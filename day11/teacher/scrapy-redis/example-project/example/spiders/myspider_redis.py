from scrapy_redis.spiders import RedisSpider

#MySpider继承RedisSpider
class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    #爬虫名称，在redis数据库的时候，
    name = 'myspider_redis'
    #添加起始路径的时候：lpush  myspider:start_urls 起始路径
    redis_key = 'myspider:start_urls'


    allowed_domains = ['atguigu.com']
    # def __init__(self, *args, **kwargs):
    #     # Dynamically define the allowed domains list.
    #     domain = kwargs.pop('domain', '')
    #     self.allowed_domains = filter(None, domain.split(','))
    #     super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
