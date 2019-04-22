import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth
params={'firstname':'li','lastname':'daxian'}
r=requests.post('http://pythonscraping.com/pages/files/processing.php',data=params)
print(r.text)

#files={'uploadFile':open('.../wenjian.png','rb')}#打开本机文件，rb打开，上传
#r=requests.post('http://pythonscraping.com/pages/processing2.php',files=files)
#print(r.text)
params={'username':'li','password':'password'}
r=requests.post('http://pythonscraping.com/pages/cookies/welcome.php',params)
#r=requests.get('http://pythonscraping.com/pages/cookies/profile.php',cookies=r.cookies)
print(r.text)


import requests
session=requests.Session()#保持cookie在线
params={'username':'username','password':'password'}
s=session.post('http://pythonscraping.com/pages/cookies/welcome.php',params)
s=session.get('http://pythonscraping.com/pages/cookies/profile.php')
print(s.text)


#HTTP基本接入认证
auth=HTTPBasicAuth('ruan','password')
r=requests.post(url='http://pythonscraping.com/pages/auth/login.php',auth=auth)
print(r.text)