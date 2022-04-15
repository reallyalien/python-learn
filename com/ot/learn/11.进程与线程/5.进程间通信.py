'''

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。

我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据：
'''

from multiprocessing import Process, Queue
import os, time, random


def write(queue):
    print("写数据开始：%s" % os.getpid())
    for value in ['A', 'B', 'C']:
        queue.put(value)
        time.sleep(random.random() * 10)


def read(queue):
    print("读数据开始：%s" % os.getpid())
    while 1:
        value = queue.get(1)
        print("从队列当中获取数据%s" % value)


if __name__ == '__main__':
    q = Queue()
    w = Process(target=write, args=(q,))
    r = Process(target=read, args=(q,))
    w.start()
    r.start()
    w.join()
    r.terminate()
