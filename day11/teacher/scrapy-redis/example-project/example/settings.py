# Scrapy settings for example project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
SPIDER_MODULES = ['example.spiders']
NEWSPIDER_MODULE = 'example.spiders'

#模拟浏览器身份
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'

#使用scrapy_redis自己的去重处理器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
#使用scrapy_redis自己调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
#爬虫可以暂停/开始， 从爬过的位置接着爬取
SCHEDULER_PERSIST = True

#不设置的话，默认使用的是SpiderPriorityQueue

#优先级队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
#普通队列
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
#栈
#SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

ITEM_PIPELINES = {
    #scrapy默认配置
    'example.pipelines.ExamplePipeline': 300,
    #把数据默认添加到redis数据库中
    'scrapy_redis.pipelines.RedisPipeline': 400,
}

#日志基本
LOG_LEVEL = 'DEBUG'

# Introduce an artifical delay to make use of parallelism. to speed up the
# crawl.
#下载延迟1秒
# DOWNLOAD_DELAY = 1


#配置redis数据库信息

#redis数据库主机---
REDIS_HOST = "192.168.28.24"
#redis端口
REDIS_PORT = 6379
