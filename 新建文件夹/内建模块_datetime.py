from datetime import datetime,timedelta,timezone
import re
m=datetime.now()#现在的时间
r='2015-1-21 9:01:30'
n=m.timestamp()#datetime转换为timestamp
a=datetime.fromtimestamp(n)#timestamp转换为datetime
b=datetime.utcfromtimestamp(n)#timestamp转换为utc标准时间
c=datetime.strptime(r,'%Y-%m-%d %H:%M:%S')#str转换为标准时间
d=m.strftime('%Y-%m-%d %H:%M:%S')#标准时间变为str
e=m+timedelta(days=1,hours=10)#时间加减
f=m.replace(tzinfo=timezone(timedelta(hours=8)))#本地时间转换为utc时间,默认的utc时间改变，原本的utc改为8
g=datetime.utcnow().replace(tzinfo=timezone.utc)#utc时间，强制转换为0：00
h=m.astimezone(timezone(timedelta(hours=9)))#任意时区时间转换


def to_timestamp(dt_str,tz_str):
    u=re.match(r'(utc|UTC)([+|-]\d{1,2}):00',tz_str).group(2)
    v=datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    w=v.replace(tzinfo=timezone(timedelta(hours=int(u))))
    return w.timestamp()

print(to_timestamp('2015-6-1 08:10:30','utc+5:00'))
#dt_str.replace()只是强制设置时区而不是强制转换
#dt_str.astimezone()只能强制转换已被replace过得，即带utc时间的