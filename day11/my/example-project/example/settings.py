# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

# 浏览器身份
USER_AGENT = 'scrapy-redis (+https://github.com/rolando/scrapy-redis)'

# scrapy-redis  的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# scrapy-redis 的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 爬虫可以暂停，从暂停的位置继续爬
SCHEDULER_PERSIST = True
# 优先级队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 队列FIFO 先进先出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈FILO 先进后出
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    'example.pipelines.ExamplePipeline': 300,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
# 下载延迟
DOWNLOAD_DELAY = 1

# 下面是自己指定redis相关信息主机信息,不能写错
REDIS_HOST = "localhost"
REDIS_PORT = 6379
