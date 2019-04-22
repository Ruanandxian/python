import requests
r=requests.get('https://www.douban.com/',params={'q':'python','cat':'1001'})#params传入参数
r.url#查看
r.encoding#查看编码格式
r.content#获取bytes对象
r.json()#对于json对象，可以直接获取
r=requests.get('https://www.douban.com/',headers={'User-Agent','Mozilla/6.0(iPhone;CPU iPhone OS 8_0like Mac OS x)AppleWebKit'})#传入一个http header
#发送post请求时
r.requests.post('https://accounts.douban.com/login',data={'form_email':'1204628226@qq.com','form_password':'123456'})#传入一个data


#json数据，可以直接传入
params={'key':'value'}
r.requests.post('https://www.douban.com/',json=params)#内部自动序列化为json
#如果是复杂的编码格式
upload_files={'files':open('report.xls','rb')}
r.requests.post('https://www.douban.com/',files=upload_files)


r.headers#获取响应头
r.headers['Content-Type']#响应头的某一个参数

#获取cookies
r.cookies['cs']

#传入cookies
cs={'token':'123456','status':'working'}
r=requests.get('https://www.douban.com/',cookies=cs)

#指定超时时间
r=requests.get('https://www.douban.com/',timeout=2.5)


