import chardet
print(chardet.detect(b'hello word'))#{'encoding': 'ascii', 'confidence': 1.0, 'language': ''}
data='可能我撞了南墙才会回头吧'.encode('gbk')
print(chardet.detect(data))#{'encoding': 'GB2312', 'confidence': 0.99, 'language': 'Chinese'}
data='可能我撞了南墙才会回头吧'.encode('utf-8')
print(chardet.detect(data))#{'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
