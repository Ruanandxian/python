from multiprocessing import Process
import os
def run_proc(name):
    print('run child process %s'%os.getpid())

if __name__=='__main__':
    print('parent prcess %s'%os.getpid())
    p=Process(target=run_proc,args=('fjfjfk',))
    print('child will start')
    p.start()
    p.join()
    print('end')
