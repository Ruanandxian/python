import time
import threading
def loop():
    print('thread %s id running...'%threading.current_thread().name)
    n=0
    while n<5:
        n=n+1
        print('tread %s >>> %s'%(threading.current_thread().name,n))
        time.sleep(1)
    print('thread %s ended '%threading.current_thread().name)

print('thread %s is running...'%threading.current_thread().name)
t=threading.Thread(target=loop,name='loop Thread')
t.start()
t.join()
print('thread %s ended'%threading.current_thread())