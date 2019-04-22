from multiprocessing import Process,Queue
import os,time,random

def write(q):#写数据
    print('Process to write %s'%os.getpid())
    for value in ['a','b','c']:
        print('put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())

def read(q):#读数据
    print('Process to read %s'%os.getpid())
    while True:
        value=q.get(True)
        print('get %s from queue'%value)

if __name__=='__main__':
    q=Queue()#父进程创建Queue，并传给各个子进程
    pw=Process(target=write,args=(q,))
    pr=Process(target=read,args=(q,))
    pw.start()#启动子进程写
    pw.join()#子进程关闭
    pr.start()#启动子进程读
    pr.join()#子进程关闭
    pr.terminate()#强制关闭读（pr）进程
