from scrapy import cmdline


cmdline.execute('scrapy crawl Atguigu -o atguigu.json'.split())
cmdline.execute('scrapy crawl Atguigu -o atguigu.csv'.split())