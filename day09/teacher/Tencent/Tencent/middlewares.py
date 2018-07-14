# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from Tencent.settings import USER_AGENTS,PROXY_LIST

import random



class RandomProxySpiderMiddleware(object):
    """随机代理"""

    def process_request(self, request, spider):
        #随机获取浏览器身份
        #{"ip_port":"122.114.31.177:808","user_password":None},
        #{"ip_port":"115.28.141.184:16817","user_password":"trygf521:a4c4avg9"},
        proxy = random.choice(PROXY_LIST)
        print("proxy====",proxy)
        if proxy["user_password"] is not None:
            #有账号和密码的代理服务器
            #http://username:password@some_proxy_server:port
            proxy_servie_url = "http://%s@%s" % (proxy["user_password"],proxy["ip_port"])
            print("proxy_servie_url====", proxy_servie_url)
            request.meta["proxy"] = proxy_servie_url
        else:
            #没有账号和密码
            #http://some_proxy_server:port
            proxy_servie_url = "http://%s" % (proxy["ip_port"])
            print("proxy_servie_url====", proxy_servie_url)
            request.meta["proxy"] = proxy_servie_url

        return None

class RandomUserAgentSpiderMiddleware(object):

    def process_request(self, request, spider):
        #随机获取浏览器身份
        user_agent = random.choice(USER_AGENTS)
        print("user_agent==============",user_agent)

        # request.headers.setdefault("User-Agent",user_agent)
        #注意，在pyhton3这么使用
        request.headers['User-Agent'] = user_agent


        return None


class TencentSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TencentDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
