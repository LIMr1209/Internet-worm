import requests

image_url = 'http://mm.chinasareview.com/wp-content/uploads/2017a/07/21/05.jpg'
headers = {

    'Host': 'mm.chinasareview.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': '__jsluid=28e61777c7e34ef50704f1dc59e8da96',
    'Range': 'bytes=294882-294882',
    'If-Range': '"364a3ea2724ed31:108f"',
}
response = requests.get(image_url,headers=headers)
print(response.status_code)
if response.status_code:
    with open('01.jpg','wb') as f:
        f.write(response.content)