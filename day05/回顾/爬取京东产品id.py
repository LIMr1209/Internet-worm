import requests
from bs4 import BeautifulSoup

url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&suggest=2.his.0.0&wq=&pvid=1b18505417844d23af9875c421b8e153'

headers = {
    "Host": "search.jd.com",
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Referer": "https://www.jd.com/",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "ipLoc-djd=1-72-2799-0; __jdu=15263763698291846045837; user-key=31f8cb0a-e3c6-4cda-8295-d05df30785f5; cn=0; PCSYCityID=1; dmpjs=dmp-d5926797ffe36e4306bf3ad5ace984f660628aa; TrackID=1zpoAmsl4f909tHsou-7p1-j2mcf1e7Xnnqv1U2T7ZbnPmGgsh6MVx64tIF6p9t6PaQUR03zkcby_Y2A-VhKHTZpcw3jrkjyDnxB0IN-9WDc; pinId=Wrs6UF9apuPvb2HPPQggXbV9-x-f3wj7; pin=jd_6401bf627e067; unick=%E4%B8%80%E5%8F%AA%E7%89%B9%E7%AB%8B%E7%8B%AC%E8%A1%8C%E7%9A%84%E7%8C%ABJD; _tp=YsSMrRJFO3zSogROj%2FBuRAswEyb93subxF%2BQFzCSh78%3D; _pst=jd_6401bf627e067; xtest=1.cf6b6759; qrsc=3; unpl=V2_ZzNtbRFQRBVwDBIAfR5cDWIDQApKUxcXfQ5HVnkfCFY3AhYKclRCFXwUR1JnGFsUZwYZXEFcRhJFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VH8aWwdhBBBaSl5AHXUBQ1N6HFgMZQUibUVncyVwCURQexxsBFcCIh8WC0UWcg5FVDYZWAZgARRaQFBLHHYARl1%2bHl0AYwoQW3JWcxY%3d; __jdv=122270672|baidu|-|organic|not set|1530863055828; shshshfpa=9b1d8800-feef-57c5-02f6-8fba6d667ad0-1530863059; shshshfpb=1d2614e51c0524b9d8897133092473852571820aa279ec61a5b3c41085; shshshfp=ce4c38c9bba8edd7292a8d1a7d3d9c11; 3AB9D23F7A4B3C9B=FFEHSQNBKKZV6CF2PRVWTIUC45X2IDWKSFUOIN7SIXHLLT5HGJUAZ56OZBOXCFXEOY4EDCVMNDRPMIHP2OAB7KPDHA; __jda=122270672.15263763698291846045837.1526376369.1530879728.1530924093.11; __jdc=122270672; __jdb=122270672.2.15263763698291846045837|11.1530924093; shshshsID=2e6373ca1d2d70fe29e2b56dca26027a_1_1530924102170; rkv=V0000",
}

response = requests.get(url,headers=headers)

html = response.content

soup = BeautifulSoup(html,'lxml')

tag_list = soup.select('.p-img')

id_list = []

for tag in tag_list:
    if tag.a['href'].__contains__('//item.jd.com/'):
        id_list.append(tag.a['href'].replace('//item.jd.com/','').replace('.html',''))

print(id_list)


