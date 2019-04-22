from urllib import request,parse
import urllib
import ssl
#Get
with request.urlopen('http://image.so.com/v?src=360pic_strong&z=1&i=0&cmg=b9f3d6c669faa5c714935b91a4611690&q=360%E5%9B%BE%E5%BA%93&correct=360%E5%9B%BE%E5%BA%93&cmsid=5ef0d643c861f02f84a00ed68784f8ee&cmran=0&cmras=6&cn=0&gn=0&kn=0#multiple=0&gsrc=1&dataindex=10&id=a70a0ee225397ca13294a117a747ccd8&currsn=0&jdx=10&fsn=60') as f:
    data=f.read()
    print('Status',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s:%s'%(k,v))
    print('Data',data.decode('utf-8'))
    #对一个url进行抓取，并返回响应

req=request.Request('http://www.baidu.com/')
req.add_header('User-Agent','Mozilla/6.0(iPhone;CPU iPhone OS 8_0like Mac OS x)AppleWebKit/536.26(KHTML,likeGecko)Version/8.0Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as d:
    print('Status',f.status,f.reason)
    for k,v in d.getheaders():
        print('%s:%s'%(k,v))
    print('Data',d.read().decode('utf-8'))
    #模拟iphone6 访问请求

#Post
print('login to weibo.cn...')
email=input('email:')
passwd=input('password:')
login_data=parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%1Fm.weibo.cn%2F')
])
reg=request.Request('https://passport.weibo.cn/sso/login')
reg.add_header('Origin','https://passport.weibo.cn')
reg.add_header('User-Agent','Mozilla/6.0(iPhone;CPU iPhone OS 8_0like Mac OS x)AppleWebKit/536.26(KHTML,likeGecko)Version/8.0Mobile/10A5376e Safari/8536.25')
reg.add_header('Referer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%1Fm.weibo.cn%2F')

with request.urlopen(reg,data=login_data.encode('utf-8'),context=ssl._create_unverified_context()) as x:
    print('Status',f.status,f.reason)
    for k,v in x.getheaders():
        print('%s:%s'%(k,v))
    print('Data',x.read().decode('utf-8'))
    #模拟登陆微博

#Handler
#proxy_handler=urllib.request.ProxyHandler({'http':'http://www.example.com:3128/'})
#proxy_auth_handler=urllib.request.ProxyBasicAuthHandler()
#proxy_auth_handler.add_password('realm','host','username','password')
#opener=urllib.request.build_opener(proxy_handler,proxy_auth_handler)
#with opener.open('http://www.example.com/login.html') as v:
#    pass
    #不用重点掌握