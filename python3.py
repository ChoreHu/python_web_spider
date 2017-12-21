import urllib.request

# 加载一定的时间,如果超过timeout的时间则停止加载
response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
print(response.read())