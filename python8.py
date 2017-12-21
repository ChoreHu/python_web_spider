# 添加请求头的第二种方式
from urllib import request,parse

url = 'http://httpbin.org/get'
dict = {
    'name': 'Germey'
}
# 将信息转换成bytes对象 传输的数据必须是data才行
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, method='POST')
# 给请求头对象添加头信息
req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
response = request.urlopen(req)
print(response.read().decode('utf-8'))