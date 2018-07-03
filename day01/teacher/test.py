from urllib import parse
from urllib.request import Request,urlopen


def save_page(filname,data):
	print("正在保存：",filname)
	with open(filname,'wb') as f:
		f.write(data)

	print('保存完成',filname)

def downlode_page(full_pn):
	print("正在下载：",full_pn)
	hearders={
		"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36"

	}
	req = Request(full_pn,headers=hearders)
	res = urlopen(req)
	return res.read()

def baidu_test(url,start_page,end_page):
	for page in range(start_page,end_page+1):
		pn=(page-1)*50
		full_pn =url+"&pn"+str(pn)
		print(full_pn)
		content = downlode_page(full_pn)
		print("type==",type(content))
		filname = "第"+str(page)+"页.html"
		save_page(filname,content)



def main():
	kw = input("爬取的名称：")

	start_page = int(input("起始："))
	end_page =input("结尾：")
	kw = {"kw":kw}
	kw = parse.urlencode(kw)
	url = "https://tieba.baidu.com/f?"+kw+"&ie=utf-8"
	print(url)
	baidu_test(url,start_page,end_page)

if __name__ == '__main__':
	main()
