from urllib.request import Request, urlopen

url = 'https://home.jd.com'

headers = {
    "host": "home.jd.com",
    "connection": "keep-alive",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "user-agent": "mozilla/5.0 (windoWS NT 10.0; WOW64) apPleWebKit/537.36 (KHTMl, liKe geckO) chrome/67.0.3396.99 safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "referer": "https://www.jd.com/",
    # "accept-encoding": "gzip, deflate, br",
    "accept-language": "ZH-cn,zh;q=0.9",
    "cookie": "ipLoc-djd=1-72-2799-0; __jdu=15263763698291846045837; user-key=31f8cb0a-e3c6-4cda-8295-d05df30785f5; cn=0; PCsycITyID=1; dmpjs=dmp-d5926797ffe36e4306bf3ad5ace984f660628aa; uSerinfoaccountclouds=1; unPl=V2_zzNtBUdXS0f0DkaaEHlYAMIFFFRkVrDgCQphv3sdWGW1AbpVCLRcFXwUr1JnGFkuZGSZxEnCQXRFChzXCHByAWccgLLYBBNnIEWHDCRSBUE3xHXCFVUWf3rAtWEoSVoaYWtBDKZUfBYHW0IaKELVVTUFr21YveMldQL2vH8awWDHbBbaSL5AHXUBQ1N6HFGMzqUIbuvNcYVYAejveXLsBFcCIH8WC0YqFQLEUDYZwAZGaRRAQFBLHHyARl1%2bHL0aYWoQW3jWcxy%3d; __jda=122270672.15263763698291846045837.1526376369.1530612935.1530666016.5; __jdc=122270672; ceshi3.com=000; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_419e077e0156477893eb53021578c299|1530666910679; trACkId=1Zpoamsl4f909thsou-7p1-j2mcf1e7xnnQv1U2t7ZbNpmggSH6MVx64tiF6p9t6PAQUr03zkcBy_Y2a-VHKhtzpcw3jrKjyDnXB0IN-9WDc; PinId=WRS6uf9ApuPVB2HppQgGXbv9-x-f3wj7; pin=jd_6401bf627e067; unicK=%E4%B8%80%E5%8F%AA%E7%89%B9%E7%AB%8B%E7%8B%AC%E8%A1%8C%E7%9A%84%E7%8C%ABJd; thor=4535C2223EFA8E441B9F723D683939263F9B4382A88040AE39C1686E629B3FE772F16476D03FA5245008317E55731E15BC54662BDA22C4C69C6F34F6E2DCE9A9ECB13C47928250D33D81CF7BA83A37528C5163FCDA5BE3B94BB29FB800243643AABF069770A4C2ED2B13419E4CDCF6276C4C5366166175F4064416BD5FD4E4F09856DBBFB15294CE6CC626829EEA13EEC47B6D9D27EB4AEE8E15C035807A7F7B; _Tp=YsSMRRJfO3zSOgROJ%2FBurAswEyb93sUbxF%2bQFzCSh78%3D; _pst=jd_6401bf627e067; __jdb=122270672.17.15263763698291846045837|5.1530666016; 3AB9D23F7A4B3C9B=3EXJLGG4UYPDEDNBOTSXMXQZUVX32SEKWFTXGE46WEWUM2CGLLNEBKCHIPLV3GLD7WU2RZ3UCE5VJKALZLXKCTC66U",
}

request = Request(url, headers=headers)

response = urlopen(request)

print(response.read().decode())
