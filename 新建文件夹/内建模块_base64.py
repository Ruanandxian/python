import base64
base64.b64encode(b'binary\x00string')#b'YmluYXJ5AHN0cmluZw=='
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')#b'binary\x00string'
base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')#b'abcd++//'
base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')#b'abcd--__'
base64.urlsafe_b64decode(b'abcd--__')#b'i\xb7\x1d\xfb\xef\xff'
def safe_base64_decode(s):
    while (len(s)%4)!=0:
        s=s+b'='
    return base64.urlsafe_b64decode(s)
#文本字符是3个字节倍数的情况下，=自动去掉
#01001101,01100001,01101110 ascii码转换为二进制
#010011,010110,000101，101110，四个为一组，
#19,22,5,46，十进制数
#不够24位的情况下，补0