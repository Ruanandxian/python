import random,time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

#send queue发送数据
task_queue=queue.Queue()
#receiver queue接受数据
result_queue=queue.Queue()

#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass
#注册2个queue到网络上使用callable和匿名函数关联了Queue对象
#仅适用于linux   windows下callable不能使用匿名函数
def return_task_queue():
    global task_queue
    return task_queue

def return_result_queue():
    global result_queue
    return result_queue

def runf():
    QueueManager.register('get_task_queue',callable=return_task_queue)
    QueueManager.register('get_result_queue',callable=return_result_queue)

    #设定IP，绑定端口，验证码
    manager=QueueManager(address=('192.168.54.17',5000),authkey=b'abx')

    manager.start()#启动
    task=manager.get_task_queue()#获得通过网络访问的QUeue对象
    result=manager.get_result_queue()

    #放几个任务进去
    for i in range(10):
        n=random.randint(0,10000)
        print('put task %d...'%n)
        task.put(n)

    print('TRY get results...')
    for i in range(10):
        r=result.get(timeout=10)
        print('Result:%s'%r)

    manager.shutdown()
    print('master exit')

if __name__=='__main__':
    freeze_support()
    runf()