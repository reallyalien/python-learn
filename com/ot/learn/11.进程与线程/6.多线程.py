'''
我们前面提到了进程是由若干线程组成的，一个进程至少有一个线程。

由于线程是操作系统直接支持的执行单元，因此，高级语言通常都内置多线程的支持，Python也不例外，并且，Python的线程是真正的Posix Thread，而不是模拟出来的线程。

Python的标准库提供了两个模块：_thread和threading，_thread是低级模块，threading是高级模块，对_thread进行了封装。绝大多数情况下，我们只需要使用threading这个高级模块。

启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行：
'''
import time, threading


def loop():
    print('线程：%s is running ' % threading.currentThread().getName())
    n = 0
    while n < 5:
        n += 1
        print('线程: %s >>> %s' % (threading.currentThread().getName(), n))
        time.sleep(1)
    print('线程: %s 结束.' % threading.currentThread().getName())


print('线程: %s is running...' % threading.currentThread().getName())
t = threading.Thread(target=loop, name='loop')
t.start()
t.join()
print('线程: %s 结束.' % threading.currentThread().getName())

# 由于任何进程默认就会启动一个线程，我们把该线程称为主线程，主线程又可以启动新的线程，Python的threading模块有个current_thread()函数，
# 它永远返回当前线程的实例。主线程实例的名字叫MainThread，子线程的名字在创建时指定，我们用LoopThread命名子线程。名字仅仅在打印时用来
# 显示，完全没有其他意义，如果不起名字Python就自动给线程命名为Thread-1，Thread-2……
