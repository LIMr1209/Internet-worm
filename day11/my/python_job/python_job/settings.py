# -*- coding: utf-8 -*-

# Scrapy settings for python_job project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'python_job'

SPIDER_MODULES = ['python_job.spiders']
NEWSPIDER_MODULE = 'python_job.spiders'

USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
]

# 使用scrapy_redis自己的去重处理器
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 使用scrapy_redis自己调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 爬虫可以暂停/开始， 从爬过的位置接着爬取
SCHEDULER_PERSIST = True

# 不设置的话，默认使用的是SpiderPriorityQueue

# 优先级队列
SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderPriorityQueue"
# 普通队列
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderQueue"
# 栈
# SCHEDULER_QUEUE_CLASS = "scrapy_redis.queue.SpiderStack"

# redis数据库主机---
REDIS_HOST = "localhost"
# redis端口
REDIS_PORT = 6379

# 配置mongodb相关配置
MONGODB_HOST = "localhost"
MONGODB_PORT = 27017

# 数据库名称
MONGODB_DBNAME = "job"
SHEETE_NAME = "job_items"

# mysql配置
MYSQL_HOST = "localhost"
MYSQL_PORT = 3306

MYSQL_DBNAME = "job"
TABLE_NAME = "job_items"

MYSQL_USER = "root"
MYSQL_PASSWORD = "root"
# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOADER_MIDDLEWARES = {
    'python_job.middlewares.UserAgentSpiderMiddleware': 543,
    'python_job.middlewares.ProxySpiderMiddleware': 543,
}
PROXY_LIST = [
    # {'ip_port': '115.28.141.184:16817', 'user_password': 'trygf521:a4c4avg9'},
    # {'ip_port': '119.136.145.159:808', 'user_password': None},
    {'ip_port': '49.74.91.98:53281', 'user_password': None},
    {'ip_port': '117.85.80.16:8118', 'user_password': None},
]

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'python_job.pipelines.ExamplePipeline': 300,
    'python_job.pipelines.PythonJobMogoDbPipeline': 301,
    'python_job.pipelines.PythonJobMySqlPipeline': 302,
    'scrapy_redis.pipelines.RedisPipeline': 400,
}
