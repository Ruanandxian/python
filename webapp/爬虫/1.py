from urllib.request import urlopen
html=urlopen('http://www.hrxy.com/')
print(html.read())
