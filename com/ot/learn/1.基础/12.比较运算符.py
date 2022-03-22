import time

t1 = time.gmtime()
t2 = time.gmtime()
# 每次调方法都会返回不同的对象
# == 用来比较两个变量的值是否相等，而 is 则用来比对两个变量引用的是否是同一个对象，例如：
print(t1 == t2)
print(t1 is t2)
print(t1)
