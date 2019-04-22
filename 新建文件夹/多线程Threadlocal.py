import threading
local_school=threading.local()#全局变量，各函数修改互不影响

def process_student():
    std=local_school.student
    print('Hello %s(in %s)'%(std,threading.current_thread().name))


def process_thread(name):
    local_school.student=name
    process_student()

t1=threading.Thread(target=process_thread,args=('alll',),name='Thread-A')
t2=threading.Thread(target=process_thread,args=('bbbb',),name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()
