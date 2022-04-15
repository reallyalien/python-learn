# 如果要启动大量的子进程，可以用进程池的方式批量创建子进程：

from multiprocessing import Process, Pool
import os, time, random


def long_time_task(name):
    print("进程id：%s" % os.getpid())
    start = time.time()
    time.sleep(random.random() * 10)
    end = time.time()
    print("进程id：%s 执行了%s秒" % (os.getpid(), int((end - start))))


if __name__ == '__main__':
    print("main id %s" % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))

    # 对Pool对象调用join()方法会等待所有子进程执行完毕，调用join()之前必须先调用close()，调用close()之后就不能继续添加新的Process了。
    p.close()
    p.join()
    print('所有进程都执行完')
