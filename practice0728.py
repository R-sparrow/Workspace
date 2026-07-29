'''
from urllib.request import HTTPPasswordMgrWithDefaultRealm, HTTPBasicAuthHandler, build_opener
from urllib.error import URLError


username = 'admin'
password = 'admin'
url = 'https://ssr3.scrape.center/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None, url, username, password)      #第一个参数 realm 填 None：表示使用默认的认证域（Realm）。
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)


'''
'''
import http.cookiejar
import urllib.request


cookie = http.cookiejar.CookieJar()     #用于保存Cookie
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
for item in cookie:
    print(item.name + "=" + item.value)
'''

'''
filename = 'cookie.txt'
cookie = http.cookiejar.LWPCookieJar(filename)   #创建一个能够将 Cookie 保存到本地文件，或从本地文件读取 Cookie 的容器对象。
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)
'''

'''
cookie = http.cookiejar.LWPCookieJar()  
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('https://www.baidu.com')
print(response.read().decode('utf-8'))
'''

from urllib import request, error

try:
    response = request.urlopen('https://Raven.com/404')
except error.URLError as e:
    print(e.reason)