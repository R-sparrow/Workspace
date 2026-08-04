import requests



'''
r = requests.get('https://www.baidu.com')
print(r.cookies)
for key,value in r.cookies.items():
    print(key + '=' + value)
'''

'''
import requests

headers = {
    'Cookie':'_octo=GH1.1.391043230.1775294340; _device_id=9a2dce26eb41a208d2352256d73d6a46; GHCC=Required:1-Analytics:1-SocialMedia:1-Advertising:1; MicrosoftApplicationsTelemetryDeviceId=3cb5c27d-ce59-405f-adf4-0769df1df350; MSFPC=GUID=cb4f02c211bc46bda09e776ce474b13c&HASH=cb4f&LV=202603&V=4&LU=1774522635052; saved_user_sessions=72330008%3Aw0Y2CSqaQe40G9CQ77i4jtytsMRyqrWrnef0MrnrKO4mfT5D; user_session=w0Y2CSqaQe40G9CQ77i4jtytsMRyqrWrnef0MrnrKO4mfT5D; __Host-user_session_same_site=w0Y2CSqaQe40G9CQ77i4jtytsMRyqrWrnef0MrnrKO4mfT5D; logged_in=yes; dotcom_user=R-sparrow; dashboard_surface_empty_sections=review-requested,merge-queue,waiting-for-review,needs-action,team-review-requested,ready-to-merge,your-drafts; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; cpu_bucket=xlg; preferred_color_mode=light; tz=Asia%2FShanghai; _gh_sess=3fK3IpcYrCkfAs7JkxTsNc1ntshTcOjCohn77%2BOEOXhULyBSQeiTXXUEXhTCgq52pQLilXONJAdPgHAtolv7fIsdC9Qh%2FqhcR4Xeetu39ocqznnukLRGAdSwVhQku%2BiuElM1lkyhebhzCOObN35AMjsLgEB7c1qOOQzcHtDUWcJi18i3fmft5y1sZKbvZbEJVzoekRno51KtWikH9%2BuF%2FXmMP1sTfX%2Fcu8VWN%2BNAecE5OCl2D7BXvG9ameWBvx5LaO5iL5UxCm4Nq0mPj26FJ%2BWyN8a25CKxIfcHZR%2F%2BEMUqVjBEhESoCN%2FcDESQmKBQmTKweIrK35Jo3ubp3NcdN2ypCWdGH4Io3Z85%2FwNkh%2F%2Bm8C6LziTgfDkHnOGEjavT--WxATyArICUySTkjt--h3KN%2F%2FsXDsMzbnz6YYOd0Q%3D%3D',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.0.0 Safari/537.36 Edg/147.0.0.0',
     
    
}
r = requests.get('https://github.com/', headers=headers)
print(r.text)
if "R-sparrow" in r.text:
    print("✅ 登录成功！已识别到用户名 R-sparrow")
if 'name="user-login"' in r.text:
    print("✅ 验证成功：包含 user-login 登录标头")

'''

'''
import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)
'''


import requests

proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'

}

r = requests.get('https://www.httpbin.org/get', proxies=proxies)
print(r.text)