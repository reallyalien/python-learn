# 在一个list中，删掉偶数，只保留奇数，
l1 = list(range(1, 11))


def odd(x):
    return x % 2 == 1


a = filter(lambda x: x % 2 == 1, l1)
print(list(a))
print(type(a))  # <class 'filter'>

# 把一个序列中的空字符串删掉，可以这么写：

l2 = ['', 'abc', 'hello']

b = filter(lambda x: x and x.strip(), l2)
print(list(b))
# 注意到filter()函数返回的是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。


s = " hello world "
print(len(s))
print(len(s.strip()))
