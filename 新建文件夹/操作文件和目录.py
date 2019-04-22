import os
#os.path.abspath('.')#获取当前的路径信息
#os.path.join('D:\\pycharm\\新建文件夹','join')#生成完整的路径信息
#os.mkdir('D:\\pycharm\\新建文件夹\\join')#创建文件夹
#os.rmdir('D:\\pycharm\\新建文件夹\\join')#删除文件夹
#os.rename('test.txt','text.py')#重命名
#os.remove('test.txt')#删除文件
#os.path.split('D:\\pycharm\\新建文件夹\\join\\test.txt')#拆分文件目录和文件，拆分后'test.txt'
#os.path.splitext('D:\\pycharm\\新建文件夹\\join\\test.txt')#拆分文件的后缀名，拆分后'test','txt'
#[x for x in os.listdir('.')if os.path.isdir(x)]#列出当前文件夹的所有目录
#[x for x in os.listdir('.')if os.path.isfile(x)and os.path.splitext(x)[1]=='.py']#列出当前目录下所有的文件