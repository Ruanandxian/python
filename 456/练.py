import json
from urllib.request import urlopen
html=urlopen('http://wallpaper.apc.360.cn/index.php?%20c=WallPaper&a=getAppsByCategory&cid=26&start=1&count=1&from=360chrome')
str=json.dumps(html)

print(str)
