# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from pymysql import connect
from pymongo import MongoClient
from python_job.settings import MONGODB_HOST,MONGODB_PORT,MYSQL_USER,MYSQL_DBNAME,MYSQL_HOST,MYSQL_PASSWORD,MYSQL_PORT,SHEETE_NAME


class ExamplePipeline(object):
    def process_item(self, item, spider):
        #当前爬取的时间
        item["crawled"] = datetime.utcnow()
        #爬虫的名称
        item["spider"] = spider.name+"_atguigu"
        return item

class PythonJobMogoDbPipeline(object):
    def open_spider(self,spider):
        mogo_cli = MongoClient(MONGODB_HOST,MONGODB_PORT)
        db = mogo_cli[MYSQL_DBNAME]
        self.collection = db[SHEETE_NAME]
    def process_item(self, item, spider):
        dict_item = dict(item)
        self.collection.insert_one(dict_item)
        return item

class PythonJobMySqlPipeline(object):
    def open_spider(self,spider):
        self.mysql_cli = connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASSWORD,
                 database=MYSQL_DBNAME, port=MYSQL_PORT,charset='utf8')
        self.cursor =self.mysql_cli.cursor()
    def close_spider(self,spider):
        self.cursor.close()
        self.mysql_cli.close()
    def process_item(self, item, spider):
        s = dict(item)
        params = [s["url"], s["title"], s["location"], s["salary"], s["company_name"], s["company_info"],
                 s["experience"], s["job_info"], s["address"], s["crawled"], s["spider"], ]

        sql = "INSERT INTO job_items(url,title,location,salary,company_name,company_info,experience,job_info,address,crawled,spider) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        self.cursor.execute(sql,params)
        self.mysql_cli.commit()
        return item