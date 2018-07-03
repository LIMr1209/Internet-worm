from urllib.request import ProxyBasicAuthHandler, HTTPPasswordMgrWithDefaultRealm, build_opener, Request

user = 'trygf521'
password = 'a4c4avg9'
server_host = '114.67.224.159:16816'
password_mgr = HTTPPasswordMgrWithDefaultRealm()
password_mgr.add_password(None, server_host, user, password)
ProxyHandler = ProxyBasicAuthHandler(password_mgr)

opener = build_opener(ProxyHandler)

url = 'http://www.atguigu.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
}
request = Request(url, headers=headers)
response = opener.open(request)
data = response.read()
print(data)
