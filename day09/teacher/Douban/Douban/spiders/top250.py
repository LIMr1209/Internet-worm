# -*- coding: utf-8 -*-
import scrapy

from Douban.items import DoubanItem


class Top250Spider(scrapy.Spider):
    name = 'top250'
    allowed_domains = ['movie.douban.com']

    offset = 0
    url = "https://movie.douban.com/top250?start="
    # start_urls = [url+str(offset)]

    cookies = {
        'll': '"108288"',
        'bid': 'DBS9s9lmt-c',
        '__yadk_uid': 'yvHMxnr7QcxJXoOHY2A8U9FLBozZgHbH',
        '_vwo_uuid_v2': 'D16CEBD0E184CD0353456AE6C25C35A96|3c53c8efc56933e10de4bb5ea58af023',
        'ap': '1',
        '_ga': 'GA1.2.549954725.1530459496',
        'ps': 'y',
        'ue': '"trygf521@126.com"',
        'push_noty_num': '0',
        'push_doumail_num': '0',
        '__utmv': '30149280.5384',
        '__utmc': '30149280',
        '__utmc': '223695111',
        '_pk_ref.100001.4cf6': '%5B%22%22%2C%22%22%2C1531465218%2C%22https%3A%2F%2Fwww.douban.com%2Faccounts%2Flogin%3Fredir%3Dhttps%253A%252F%252Fmovie.douban.com%252Ftop250%253Fstart%253D0%22%5D',
        '_pk_ses.100001.4cf6': '*',
        '__utma': '30149280.549954725.1530459496.1531462292.1531465218.15',
        '__utmb': '30149280.0.10.1531465218',
        '__utmz': '',
        '	30149280.1531465218.15.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct': '/accounts/login',

        '__utma': '223695111.1072928076.1530459496.1531462292.1531465218.12',
        '__utmb': '223695111.0.10.1531465218',
        '__utmz': '',
        '	223695111.1531465218.12.4.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct': '/accounts/login',

        'dbcl2': '"53849586:akpcI99vAMw"',
        'ck': 'Gpk9',
        'ct': 'y',
        '_pk_id.100001.4cf6': '6edcdabd4684e991.1530459501.12.1531466714.1531462768.',



    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',

    }


    def start_requests(self):
        yield scrapy.Request(self.url+str(self.offset),callback=self.parse,cookies=self.cookies,headers=self.headers)



    def parse(self, response):
        print("response.url===",response.url)

        all_node = response.xpath('//div[@class="info"]')
        for node in all_node:

            item = DoubanItem()
            print("--"*100)
            #影片的标题
            tilte = node.xpath('.//span[@class="title"][1]/text()').extract()[0]
            #影片的信息
            content = node.xpath('.//div[@class="bd"]/p/text()').extract()[0]
            #影片的评分
            score = node.xpath('.//div[@class="star"]/span[2]/text()').extract()[0]
            #影片的一句话简介
            info = node.xpath('.//p[@class="quote"]/span/text()').extract()
            if len(info) > 0:
                info = info[0]

            item["tilte"] = tilte
            item["content"] = content
            item["score"] = score
            item["info"] = info

            print(item)

            yield item


        #实现下一页的功能

        if self.offset < 225:
            self.offset += 25

        next_url = self.url + str(self.offset)

        yield scrapy.Request(next_url,callback=self.parse,headers=self.headers)





