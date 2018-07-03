from urllib import parse
from urllib.request import  Request,urlopen

def save_html(file_name,html):
    print('正在保存',file_name)
    with open(file_name,'wb') as f:
        f.write(html)
    print('保存成功',file_name)

def down_html(full_url):
    headers = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;"
    request = Request(full_url)
    request.add_header('User-Agent',headers)

    response = urlopen(request)
    return response.read()


def baidu_spider(url,start_page,end_page):
    for page in range(start_page,end_page+1):
        pn = (page-1)*50
        full_url = url +'&pn='+str(pn)
        file_name = '第'+str(page)+'页.html'
        print('正在下载',full_url)
        html = down_html(full_url)
        save_html(file_name,html)

def main():
    kw = input('贴吧名：')
    start_page = int(input('开始页码：'))
    end_page = int(input('结束页码：'))
    kw = {'kw':kw}
    kw = parse.urlencode(kw)
    # url = 'https://tieba.baidu.com/f?kw=%E5%B0%9A%E7%A1%85%E8%B0%B7&pn=50'
    url = 'https://tieba.baidu.com/f?'+kw
    baidu_spider(url,start_page,end_page)

if __name__ == '__main__':
    main()