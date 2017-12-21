import urllib.parse
import urllib.request

# 将word=hello作为参数转换成bytes传递给urlopen方法
data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding="utf-8")
print(data)

# 打开对应的url,传递相应的data参数
response = urllib.request.urlopen('http://www.baidu.com/post', data=data)
print(response.read())

# 测试网站得不到请求?