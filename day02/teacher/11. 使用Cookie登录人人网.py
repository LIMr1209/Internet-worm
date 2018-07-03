from urllib.request import  Request,urlopen


url = "http://www.renren.com/964604530"

headers = {
"Host":"www.renren.com",
"Connection":"keep-alive",
"Cache-Control":"max-age=0",
"Upgrade-Insecure-Requests":"1",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"Referer":"http://www.renren.com/",
"Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"anonymid=jj4dweuc8urouu; depovince=ZGQT; _r01_=1; ln_uact=yangguangfu2017@163.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20180312/1720/h_main_rI1p_b6d2000d171a1986.jpg; jebe_key=64445fd6-45d2-4f9d-8c6c-0569db5effda%7C23d7f054f633e4326590e7719a77981f%7C1530543234521%7C1%7C1530543236882; _de=839AB3C91139E616062ACF0F25D1AE7D5BF7EAB63017E04A; jebecookies=f71382b5-bd49-445a-b902-9a4dbcc4febb|||||; JSESSIONID=abc99MMuMzjJT87NudFrw; ick_login=ed4e81ab-92a1-4989-b1ea-45eacceff8e9; p=058e5cb868c731224338da65aff0b4510; first_login_flag=1; t=be8ff8637a45c06d5914d963dc1baf640; societyguester=be8ff8637a45c06d5914d963dc1baf640; id=964604530; xnsid=a0f268d0; ver=7.0; loginfrom=null; wp_fold=0",
}
#创建request
request = Request(url,headers=headers)


response = urlopen(request)

html = response.read()

print(html.decode("utf-8"))