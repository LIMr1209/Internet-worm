from urllib.request import  Request,urlopen


url = "https://home.jd.com/"

headers = {
# "Accept-Encoding":"gzip, deflate, br",
# "Host":"home.jd.com",
# "Connection":"keep-alive",
# "Accept":"text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
# "X-Requested-With":"XMLHttpRequest",
# "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
# "Referer":"https://home.jd.com/",
# "Accept-Language":"zh-CN,zh;q=0.9",
"Cookie":"__jdv=122270672|direct|-|none|-|1530447249089; PCSYCityID=1; shshshfpa=aeb5d683-b772-ff03-8ae6-2dac71f29cf6-1530447250; shshshfpb=0b75efa47522f0f07cef09e462f624749b4502d8c036c1e6a5b38c5921; areaId=1; user-key=78b0fa39-e8ec-4436-804f-4f9579c6db0c; ipLoc-djd=1-2901-4135-0.138288412; ipLocation=%u5317%u4eac; cn=0; _distM=77289677261; _jrda=1; __jdu=1597118661; shshshfp=a94755ed07cd3e00a4a2879a98856f2f; __jda=122270672.1597118661.1530446014.1530542709.1530601518.6; __jdc=122270672; wlfstk_smdl=ak96jiy2pym99rqgsumzfuzy0t4mmipw; TrackID=1DuvqMDz09DYkrLV-jIv0lvrDsTPrzzHPsDGRqbegh0ek0wKQR9vbw3DtmCdF6f8VwzMpv11q1MHg55LfCBxHig; pinId=tF0w3lsgbrKuuR-PW68-4Q; pin=python_afu; unick=python_afu; thor=80CA3AE410CD0EC710BCA2C673334B1C8F48C5A9A332023108EA1134A96F24B06A12CE63B1CBB952E8BF0DA45C630ECA9136ADB827832BBFAD2FDEE175F796CE332BC3E3524D62A78E8AB5A04E6AB15C25FC4208804A6BB6EBECD38607DD24B3E66A7BAB29D50EEA8024DD572FB635D24636E12C25CCAE41E9CAC5809513AB04A98BA10E347A0033E05D5596BFE2C054; _tp=wmA28pFNyQS3czxsK1OIHA%3D%3D; _pst=python_afu; ceshi3.com=000; shshshsID=a6a4aa68e568ba5997390dd01d4ddc33_2_1530601542506; 3AB9D23F7A4B3C9B=3JRK7JWTXAB65RWQ7VTATRTEE5FP3SSEWYN22GGU2VEDZ3SITYGMP53UFOY3XV7YVH7SF7PSJOLRKIYIWDCK6HD2N4; userInfoaccountclouds=1; __jdb=122270672.7.1597118661|6.1530601518",

}
#创建request
request = Request(url,headers=headers)


response = urlopen(request)

html = response.read()

print(html.decode("utf-8"))