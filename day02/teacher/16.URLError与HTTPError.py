from urllib.request import Request,urlopen,URLError,HTTPError

try:
	url = "http://www.baidu.com"
	# url = "http://192.168.28.123:8080/hehhels"
	request = Request(url)

	response = urlopen(request)


except HTTPError as e:
	print("HTTPError==",e)
# 	#404错误的时候，抛出的异常
except URLError as e:
	#没有网络，或者url错误
	print("URLError==",e)

else:
	print(response.read())

