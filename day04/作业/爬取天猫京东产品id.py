import requests
from bs4 import BeautifulSoup

# url = 'https://list.tmall.com/search_product.htm?q=%D0%D8%D5%D6&type=p&vmarket=&spm=875.7931836%2FB.a2227oh.d100&xl=xio_6&from=mallfp..pc_1_suggest&smToken=c39f60cfc1c24bfbab1679cee5647a42&smSign=DU9epGJmFUEjsy1kt4ugGg%3D%3D'
#
# headers = {
#     "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "accept-language": "zh-CN,zh;q=0.9",
#     "cache-control": "max-age=0",
#     "cookie": "cna=tRgoE/vHrAECAd9HVQ4MVOMD; dnk=%5Cu658C%5Cu7237%5Cu72371058169464; uc1=cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=U%2BGCWk%2F7p4mBoUyS4E9C&cookie15=URm48syIIVrSKA%3D%3D&existShop=false&pas=0&cookie14=UoTfK7uxz%2FsLlw%3D%3D&tag=8&lng=zh_CN; uc3=vt3=F8dBzr%2FH0cd8OySBqpM%3D&id2=UU6m3oSoOMkDcQ%3D%3D&nk2=0rawKUoBrqUrgaRu025xgA%3D%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; tracknick=%5Cu658C%5Cu7237%5Cu72371058169464; lid=%E6%96%8C%E7%88%B7%E7%88%B71058169464; _l_g_=Ug%3D%3D; unb=2671514723; lgc=%5Cu658C%5Cu7237%5Cu72371058169464; cookie1=BxNSonczp%2BfH4JvkmZGiHVjnsgV7tsFybnrAAaVXt9g%3D; login=true; cookie17=UU6m3oSoOMkDcQ%3D%3D; cookie2=130702bb507f7bee3502ae7bd4e5ad61; _nk_=%5Cu658C%5Cu7237%5Cu72371058169464; t=7b20b59e85e71bc6919f77ce401dd542; sg=437; csg=653b2c52; _tb_token_=75e44e7faebf3; tt=login.tmall.com; _med=dw:1536&dh:864&pw:1920&ph:1080&ist:0; otherx=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0; swfstore=310865; x=__ll%3D-1%26_ato%3D0; enc=y82ocQbaApL8Iun%2BVb8DPfmSBmbNkVP3c7mkic6CsLSPEQCml8q7Art3nKLS0aesZpOiqAfENYuZ98VZUkarFw%3D%3D; res=scroll%3A1519*6086-client%3A1519*318-offset%3A1519*6086-screen%3A1536*864; pnm_cku822=098%23E1hvU9vUvbpvUvCkvvvvvjiPPss9zjEvR2z90jthPmP9tjrPRszptjr8PLLZsjlEiQhvCvvvpZpPvpvhvv2MMQhCvvOvChCvvvvEvpCW940h3C0QRqJ6WeCpqU0QKfUpwZ5IAfUTKFyK2ixre8TxD7QHYnp4VCI7nDeDyBvO5fh3Zi7veEQaRoxBlwyzhb8raoF6k8wghBODNdyCvm9vvhCvvvvvvvvvByOvvUvNvvCVB9vv9LvvvhXVvvmCjvvvByOvvUhwuphvmvvvpo7Y2FaHkphvC9hvpyPOz2yCvvpvvhCv; whl=-1%260%260%260; isg=BLi43jvNFyRzZ3ug_i8Sla4xiWaKiQC1XRxxavIpBPOmDVj3mjHsO84nwUUYXdSD",
#     "referer": "https://login.tmall.com/?from=sm&redirectURL=https%3A%2F%2Fsec.taobao.com%2Fquery.htm%3Faction%3DQueryAction%26event_submit_do_login%3Dok%26smApp%3Dtmallsearch%26smPolicy%3Dtmallsearch-product-anti_Spider-html-checklogin%26smCharset%3DGBK%26smTag%3DMTIxLjY5LjgxLjE2NiwsZTI1MDQ1MDBiYjYzNDg4ZThjZTI2NTMwMTczN2MxYWE%253D%26captcha%3Dhttps%253A%252F%252Fsec.taobao.com%252Fquery.htm%26smReturn%3Dhttps%253A%252F%252Flist.tmall.com%252Fsearch_product.htm%253Fq%253D%2525D0%2525D8%2525D5%2525D6%2526type%253Dp%2526vmarket%253D%2526spm%253D875.7931836%25252FB.a2227oh.d100%2526xl%253Dxio_6%2526from%253Dmallfp..pc_1_suggest%26smSign%3DP5yWlqSGC5fX7deOPLCM4Q%253D%253D",
#     "upgrade-insecure-requests": "1",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
# }
#
# response = requests.get(url, headers=headers)
#
# html = response.content
#
# soup = BeautifulSoup(html, 'lxml')
#
# id_list = []
#
# tag_list = soup.select('.product')
# for tag in tag_list:
#     id_list.append(tag['data-id'])
# print(id_list)

url = 'https://search.jd.com/Search?keyword=%E8%83%B8%E7%BD%A9&enc=utf-8&wq=%E8%83%B8%E7%BD%A9&pvid=79709ef405fa45e2bbc253e9fc12213b'
headers = {
    "Host": "search.jd.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "ipLoc-djd=1-72-2799-0; __jdu=15263763698291846045837; user-key=31f8cb0a-e3c6-4cda-8295-d05df30785f5; cn=0; PCSYCityID=1; dmpjs=dmp-d5926797ffe36e4306bf3ad5ace984f660628aa; TrackID=1zpoAmsl4f909tHsou-7p1-j2mcf1e7Xnnqv1U2T7ZbnPmGgsh6MVx64tIF6p9t6PaQUR03zkcby_Y2A-VhKHTZpcw3jrkjyDnxB0IN-9WDc; pinId=Wrs6UF9apuPvb2HPPQggXbV9-x-f3wj7; pin=jd_6401bf627e067; unick=%E4%B8%80%E5%8F%AA%E7%89%B9%E7%AB%8B%E7%8B%AC%E8%A1%8C%E7%9A%84%E7%8C%ABJD; _tp=YsSMrRJFO3zSogROj%2FBuRAswEyb93subxF%2BQFzCSh78%3D; _pst=jd_6401bf627e067; xtest=1.cf6b6759; qrsc=3; unpl=V2_ZzNtbRFQRBVwDBIAfR5cDWIDQApKUxcXfQ5HVnkfCFY3AhYKclRCFXwUR1JnGFsUZwYZXEFcRhJFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH8aWwdhBBBaSl5AHXUBQ1N6HFgMZQUibUVncyVwCURQexxsBFcCIh8WC0UWcg5FVDYZWAZgARRaQFBLHHYARl1%2bHl0AYwoQW3JWcxY%3d; __jdv=122270672|baidu|-|organic|not set|1530863055828; shshshfpa=9b1d8800-feef-57c5-02f6-8fba6d667ad0-1530863059; shshshfpb=1d2614e51c0524b9d8897133092473852571820aa279ec61a5b3c41085; shshshfp=ce4c38c9bba8edd7292a8d1a7d3d9c11; 3AB9D23F7A4B3C9B=FFEHSQNBKKZV6CF2PRVWTIUC45X2IDWKSFUOIN7SIXHLLT5HGJUAZ56OZBOXCFXEOY4EDCVMNDRPMIHP2OAB7KPDHA; shshshsID=39df413ff6a04a1262138ae679d06886_1_1530879728107; __jda=122270672.15263763698291846045837.1526376369.1530863056.1530879728.10; __jdb=122270672.1.15263763698291846045837|10.1530879728; __jdc=122270672; rkv=V0000",
}

response = requests.get(url,headers=headers)
html = response.content

soup = BeautifulSoup(html,'lxml')

tag_list = soup.select('.p-img')
id_list = []
for tag in tag_list:
    id = tag.a['href']
    if id.__contains__('//item.jd.com/'):
        id_list.append(id.replace('//item.jd.com/','').replace('.html',''))
print(id_list)


