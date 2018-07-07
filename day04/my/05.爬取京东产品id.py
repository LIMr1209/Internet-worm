from urllib3 import PoolManager, disable_warnings
from bs4 import BeautifulSoup
import re

disable_warnings()

http = PoolManager()
headers = {
    "host": "search.jd.com",
    "connection": "keep-alive",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/67.0.3396.99 safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "referer": "https://search.jd.cOm/search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%ac&enc=utf-8&wQ=%E7%AC%94%E8%AE%B0%E6%9C%ac&pvid=23e7cc840c254821a91c5989ee137a34",
    "accept-language": "ZH-cn,zh;q=0.9",
    "cookie": "ipLoc-djd=1-72-2799-0; __jdu=15263763698291846045837; user-key=31f8cb0a-e3c6-4cda-8295-d05df30785f5; cn=0; PCsycITyID=1; dmpjs=dmp-d5926797ffe36e4306bf3ad5ace984f660628aA; trACkId=1Zpoamsl4f909thsou-7p1-j2mcf1e7xnnQv1U2t7ZbNpmggSH6MVx64tiF6p9t6PAQUr03zkcBy_Y2a-VHKhtzpcw3jrKjyDnXB0IN-9WDc; PinId=WRS6uf9ApuPVB2HppQgGXbv9-x-f3wj7; pin=jd_6401bf627e067; unicK=%E4%B8%80%E5%8F%AA%E7%89%B9%E7%AB%8B%E7%8B%AC%E8%A1%8C%E7%9A%84%E7%8C%ABJD; _Tp=YsSMRRJfO3zSOgROJ%2FBurAswEyb93sUbxF%2bQFzCSh78%3D; _pst=jd_6401bf627e067; unPl=V2_zzNtBUpwrKdXD0UEkE5FBWJxF1HLUUyuJLgtUNxJwWfVAhiNCLRcFXwUr1JnGFsUZWMzwUdCRHBFChzXCHByAWccgLLYBBNnIEWHDCRSBUE3xHXCFVUWf3rAtWEoSVoaYWtBDKZUfBYHW0IaKELVVTUFr21YveMldQL2vH8awWDHbBbaSL5AHXUBQ1N6HFGMzqUIbuvNcYV8AuvQfX5sBFcCIH8Wc0mcCGPAUTYZwAZGaRRAQFBLHHyARl1%2bHL0aYWoQW3jWcxy%3d; __jda=122270672.15263763698291846045837.1526376369.1530675467.1530849288.7; __jdc=122270672; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_904c562abf214e448740bad76a65901a|1530849287527; shshshfpa=d98bea14-d861-fc58-17b4-f12a42da06c7-1530849294; shshshfpb=1d2614e51c0524b9d8897133092473852571820aa279ec61a5b3c41085; xtest=1.cf6b6759; shshshfp=ce4c38c9bba8edd7292a8d1a7d3d9c11; rKv=V0000; 3AB9D23F7A4B3C9B=FFEHSQNBKKZV6CF2PRVWTIUC45X2IDWKSFUOIN7SIXHLLT5HGJUAZ56OZBOXCFXEOY4EDCVMNDRPMIHP2OAB7KPDHA; __jdb=122270672.4.15263763698291846045837|7.1530849288; shshSHsId=0a569094936543a140d5b951e975b51b_4_1530849344647; qrsc=3",
}

url = 'https://search.jd.com/Search?keyword=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&enc=utf-8&wq=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&pvid=87990569eb784c7d97e3ad26e742ad10'
response = http.request('get', url, headers=headers)

html = response.data
# html = response.data.decode()   #这两个html都行
# print(html)

soup = BeautifulSoup(html, 'lxml')

# all_link = soup.find_all(href=re.compile(r'^//item.jd.com/(\d+).html$'))
# id_list = []
#
# for link in all_link:
#     print(link['href'])
#     a = link['href'].replace('//item.jd.com/','').replace('.html','').replace('#comment','')
#     id_list.append(a)
#
# id_list = list(set(id_list))
# print(id_list)
all_link = soup.select('div[class="p-img"] a')
all=[]
for link in all_link:
    # print(link['href'])
    if link['href'].__contains__('//item.jd.com/'):
        all.append(link['href'])
print(all)
id_list = []

for link in all:
    a = link.replace('//item.jd.com/','').replace('.html','').replace('#comment','')
    id_list.append(a)

id_list = list(set(id_list))
print(id_list)




