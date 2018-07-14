# -*- coding: utf-8 -*-

# Scrapy settings for Douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Douban'

SPIDER_MODULES = ['Douban.spiders']
NEWSPIDER_MODULE = 'Douban.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Douban (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   # 'Accept-Language': 'en',
# # 'Host':'movie.douban.com',
# # 'Connection':'keep-alive',
# # 'Cache-Control':'max-age=0',
# # 'Upgrade-Insecure-Requests':'1',
# 'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
# # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
# # 'Referer':'https://www.douban.com/accounts/login?redir=https%3A%2F%2Fmovie.douban.com%2Ftop250%3Fstart%3D0',
# # 'Accept-Encoding':'gzip, deflate, br',
# # 'Accept-Language':'zh-CN,zh;q=0.9',
# # 'Cookie':'ll="108288"; bid=DBS9s9lmt-c; __yadk_uid=yvHMxnr7QcxJXoOHY2A8U9FLBozZgHbH; _vwo_uuid_v2=D16CEBD0E184CD0353456AE6C25C35A96|3c53c8efc56933e10de4bb5ea58af023; ap=1; _ga=GA1.2.549954725.1530459496; ps=y; ue="trygf521@126.com"; push_noty_num=0; push_doumail_num=0; __utmv=30149280.5384; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1531462291%2C%22https%3A%2F%2Faccounts.douban.com%2Flogin%3Falias%3Dtrygf521%2540126.com%26redir%3Dhttps%253A%252F%252Fmovie.douban.com%252Ftop250%253Fstart%253D225%2526filter%253D%26source%3DNone%26error%3D1013%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.549954725.1530459496.1531450644.1531462292.14; __utmb=30149280.0.10.1531462292; __utmz=30149280.1531462292.14.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; __utma=223695111.1072928076.1530459496.1531450644.1531462292.11; __utmb=223695111.0.10.1531462292; __utmz=223695111.1531462292.11.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/login; dbcl2="53849586:cPX1zKVrAZs"; ck=yFQN; _pk_id.100001.4cf6=6edcdabd4684e991.1530459501.11.1531462686.1531453028.',
#
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Douban.middlewares.DoubanSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'Douban.middlewares.DoubanDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Douban.pipelines.DoubanPipeline': 300,
}


#
USER_AGENTS = [
   'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36'
   'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.101 Safari/537.36 ',
]

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
