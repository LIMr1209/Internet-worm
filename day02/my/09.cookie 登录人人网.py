from urllib.request import Request,urlopen

url = 'http://zhibo.renren.com'
headers = {
    "host": "zhibo.renren.com",
    "connection": "keep-alive",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/67.0.3396.99 safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "referer": "https://www.baidu.com/link?urL=WIOElniZSARFBnC2ihc-WwmF_x6ee_F71Xuf9rqu5x_&wd=&eqid=fb1c744c0005a8f0000000035b3b4d20",
    # "accept-encoding": "gzip, deflate",
    "accept-language": "ZH-cn,zh;q=0.9",
    "cookie": "anonymid=jj3le9ma9dv3ic; depovinCE=BJ; _r01_=1; jebe_key=d92a25c2-cc9f-4cc7-99c5-96c958035acF%7C58980be99b0de10fe7adab87f46cb9d7%7C1530582242945%7C1%7C1530582247259; __utma=151146938.465862207.1530582258.1530582258.1530582258.1; __utmz=151146938.1530582258.1.1.utmcsr=zhibo.renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/top; jebecookies=8f03ffa7-0271-49c8-8e96-3b4bc5780646|||||; ick_login=38847b73-5779-46cb-a699-af087982bf14; ick=83a8a6f9-a93b-430b-a7c8-49cb5cf5d075; _dE=8A832077A64209CEBE53EDD600EBB129; p=6ef6ba9ad45bd6e328415786746e32559; first_login_flag=1; ln_uact=17635700440; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=2f604df86fd63b1f78b273de3b3af2ee9; societyguester=2f604df86fd63b1f78b273de3b3af2ee9; id=966762689; xnsid=a059b576; loginfrom=syshomE; JSESSIONid=Abcl3xvigLk1L5MTkpFrw; wp_fold=0; BAIDU_Ssp_lcr=https://www.baidu.com/link?urL=WIOElniZSARFBnC2ihc-WwmF_x6ee_F71Xuf9rqu5x_&wd=&eqid=fb1c744c0005a8f0000000035b3b4d20",
}

request = Request(url,headers=headers)

response = urlopen(request)

data = response.read()

print(data.decode())