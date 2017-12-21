import socket
import urllib.request
import urllib.error

# 对这行代码进行捕获异常
# 开启该网页,时间长度为0.1s
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
# 返回的是urllib包中的错误,如果错误原因是超时,则输出内容,确实是超时了
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')