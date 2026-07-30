

'''
from urllib import request, error

try:
    response = request.urlopen('https://Raven.com/404')
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, sep='\n')   #sep  separator  sep='\n'（按换行符分隔）
except error.URLError as e:
    print(e.reason)
else:
    print('Request Successfully')

'''


'''
from urllib.parse import urlparse

result = urlparse('https://www.baidu.com/index.html;user?id=5#comment')
print(type(result))
print(result)
'''


from urllib.parse import urlunparse
data = ['https','www.baidu.com','index.html','user','a=6','comment'] 
print(urlunparse(data))