from scrapy import cmdline
#运行爬虫
# cmdline.execute("scrapy crawl Atguigu".split())

#运行爬虫,把parse返回的数据，保存到对应的文件
cmdline.execute("scrapy crawl Atguigu -o json.json".split())


# cmdline.execute("scrapy crawl Atguigu".split())
