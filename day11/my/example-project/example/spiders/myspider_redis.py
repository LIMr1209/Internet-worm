from scrapy_redis.spiders import RedisSpider


# redis 的基本爬虫
class MySpider(RedisSpider):
    """Spider that reads urls from redis queue (myspider:start_urls)."""
    # 爬虫的名称
    name = 'myspider_redis'
    # key
    redis_key = 'myspider:start_urls'

    # allowed_domains = ['meizitu.com']

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        domain = kwargs.pop('domain', '')
        self.allowed_domains = filter(None, domain.split(','))
        super(MySpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        return {
            'name': response.css('title::text').extract_first(),
            'url': response.url,
        }
