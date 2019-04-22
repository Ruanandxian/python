from html.parser import HTMLParser
from urllib import request
import re


class MyHTMLParser(HTMLParser):
    flag = 0#建立一个标志位
    mm = []#建立一个list集合
    is_get_data = 0#建立一个存放标题

    def __init__(self):
        HTMLParser.__init__(self)#表示可以调用父类
    def handle_starttag(self, tag, attrs):#每一个开头的操作
        if tag == 'ul':
            for attr in attrs:
                if re.match(r'list-recent-events', attr[1]):#用正则表达式判断attr[1]是否与r'list-recent-events'xiangdeng
                    self.flag = 1
        if tag == 'a' and self.flag == 1:
            self.is_get_data = 'title'#给self.is_get_data一个暂时的数据
        if tag == 'time' and self.flag == 1:
            self.is_get_data = 'time'#给self.is_get_data一个暂时的数据
        if tag == 'span' and self.flag == 1:
            self.is_get_data = 'addr'#给self.is_get_data一个暂时的数据

    def handle_endtag(self, tag):#每一个结尾的操作
        if self.flag==1 and tag=='ul':
            self.flag = 0
            #标志设置为0

    def handle_data(self, data):#遇见中间data的操作
        if self.is_get_data and self.flag==1:
            if self.is_get_data=='title':
                self.mm.append({self.is_get_data: data})#只能是：
            else:
                self.mm[len(self.mm) - 1][self.is_get_data] = data
                #当前正在操作的元素减1，取出当前的元素，之后self.is_get_data=data
                #第二个self.is_get_data是time
                #self.is_get_data=data即目前的data赋给self.is_get_data
                #是一个逐渐增加元素的操作
        self.is_get_data = None
        #self.is_get_data设置为错误


parser = MyHTMLParser()
with request.urlopen('https://www.python.org/events/python-events/') as f:
    data = f.read().decode('utf-8')

parser.feed(data)
for item in MyHTMLParser.mm:#列出好几个item
    print('-----------------------------------------------------------------')
    for k,v in item.items():#item的两个attr即attrs为[{'class':'list-recent-events menu'}attrs[0],attrs[1]
        print('%s:%s'%(k,v))


