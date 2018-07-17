import json
import redis
from pymysql import connect

redis_cli = redis.StrictRedis(host='localhost', port=6379, db=0)
mysql_cli = connect(host='localhost', user='root', password="root",
                    database='sina', port=3306,
                    charset='utf8')
cursor = mysql_cli.cursor()

while True:
    source, data = redis_cli.blpop(['sinainfospider_redis:items'])
    item = json.loads(data.decode("utf-8"))
    params = [item['parent_url'], item['parent_title'], item['sub_title'], item['sub_url'], item['sub_file_name'],
              item['son_url'], item['head'], item['content'], item['son_path'], item['crawled'], item['spider']]
    sql = "insert into sinainfospider_redis_items(parent_url,parent_title,sub_title,sub_url,sub_file_name,son_url,head ,content,son_path,crawled,spider) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s )"
    cursor.execute(sql, params)
    mysql_cli.commit()
    cursor.close()
    print(item)
