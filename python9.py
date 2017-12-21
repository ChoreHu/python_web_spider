# 代理 ProxyHandler设置代理
import urllib.request

proxy_handler = urllib.request.ProxyHandler({
    'http': 'http://127.0.0.1:3128',
    'https': 'https://127.0.0.1:3128'
})
opener = urllib.request.build_opener(proxy_handler)
response = opener.open('http://www.baidu.com/get')
# 为什么代理会失败
print(response.read())