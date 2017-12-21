import urllib.request

# 接收请求命令
response = urllib.request.urlopen('http://www.baidu.com')
print(response.read().decode('utf-8'))