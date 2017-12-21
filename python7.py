# 给请求对象包裹头信息
from urllib import request, parse

url = 'http://httpbin.org/get'
# 造一个头信息模仿用户登录,发送头信息
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible;MSIE 5.5; Windows NT)',
    'Host': 'httpbin.org'
}
dict = {
    'name': 'choreHu'
}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))
