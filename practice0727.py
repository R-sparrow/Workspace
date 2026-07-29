import urllib.request
import socket
#import urllib.errozr
from urllib import request, parse

'''
response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
print (response.read())
'''

'''
try:
    response = urllib.request.urlopen('https://www.httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:                           #含义：捕获所有由网络请求失败引发的 urllib.error.URLError 错误，并将捕捉到的异常对象命名为 e
    if isinstance(e.reason, socket.timeout):                 #isinstance(A, B)：Python 内置函数，用来检查对象 A 是否是类/类型 B 的实例。
        print('TIME OUT')
'''


url = 'https://www.httpbin.org/post'
headers = {
    'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
    'Host': 'www.httpbin.org'
}
dict = {'name': 'germey'}
data = bytes(parse.urlencode(dict), encoding='utf-8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))