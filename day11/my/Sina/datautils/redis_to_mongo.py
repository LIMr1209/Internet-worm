import redis
import pymongo
import json


redis_cli = redis.StrictRedis(host='localhost',port=6379,db=0)
mongo_cli = pymongo.MongoClient(host='localhost',port=27017)

db = mongo_cli['sina']

sheet = db['sinainfospider_redis:items']

while True:
    source,data = redis_cli.blpop(['sinainfospider_redis:items'])
    item = json.loads(data.decode('utf-8'))
    print(item)
    sheet.insert_one(item)