#!/usr/bin/env python
import urllib.request

# 为什么要设置一个request对象
request = urllib.request.Request('https://python.org')
# urlopen方法既可以用字符串也可以做一个Request对象
response = urllib.request.urlopen('https://python.org')
print(response.read().decode('utf-8'))
