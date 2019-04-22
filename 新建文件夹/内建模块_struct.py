import struct
struct.pack('>l',10240099)#b'\x00T\xc5c'
#pack函数吧任意数据变成bytes
#>表示字节顺序是big-endian,也就是网络序
#l表示4字节无符号整数
struct.unpack('>lH',b'\xf0\xf0\xf0\xf0\x80\x80')#(-252645136, 32896)
#unpack把bytes变成相应的数据类型
#l表示四字节无符号整数
#H表示二字节无符号整数
d=open('D:/pycharm/新建文件夹/1.bmp','rb')
s=d.read(30)#读前30个字节b'BM\x86D\x11\x00\x00\x00\x00\x006\x00\x00\x00(\x00\x00\x003\x03\x00\x00\xcc\x01\x00\x00\x01\x00\x18\x00'
d.close()#关闭
struct.unpack('<ccllllllHH',s)#显示一个bmp图片的各种属性

#bmp格式采用小端方式存储数据，文件头的结构按顺序如下

#两个字节：BM表示windows位图，BA表示OS/2位图
#一个4字节整数：表示位图大小
#一个4字节整数：保留位，始终为0
#一个4字节整数：实际图像的偏移量
#一个4字节整数：Header的字节数
#一个4字节整数：图像宽度
#一个4字节整数：图像高度
#一个2字节整数：始终为1
#一个2字节整数：颜色数
