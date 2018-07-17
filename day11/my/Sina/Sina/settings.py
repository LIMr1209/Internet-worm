# -*- coding: utf-8 -*-

# Scrapy settings for Sina project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Sina'

SPIDER_MODULES = ['Sina.spiders']
NEWSPIDER_MODULE = 'Sina.spiders'



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

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {

   # scrapy默认配置
   'Sina.pipelines.ExamplePipeline': 300,
   'Sina.pipelines.SinaPipeline': 301,
   # 把数据默认添加到redis数据库中
   'scrapy_redis.pipelines.RedisPipeline': 400,
}

# 日志基本
LOG_LEVEL = 'DEBUG'


#配置redis数据库信息

#redis数据库主机---
REDIS_HOST = "localhost"
#redis端口
REDIS_PORT = 6379
