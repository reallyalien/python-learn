'''
如果你打算编写多进程的服务程序，Unix/Linux无疑是正确的选择。由于Windows没有fork调用，难道在Windows上无法用Python编写多进程的程序？

由于Python是跨平台的，自然也应该提供一个跨平台的多进程支持。multiprocessing模块就是跨平台版本的多进程模块。

multiprocessing模块提供了一个Process类来代表一个进程对象，下面的例子演示了启动一个子进程并等待其结束：
'''
from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('子进程id %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('父进程id %s' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('子进程启动')
    p.start()
    p.join()
    print('父进程结束')
# 创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，这样创建进程比fork()还要简单。
#
# join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
