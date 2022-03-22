from collections.abc import Iterable, Iterator


# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
def f(x):
    return x * x


l1 = list(range(1, 11))

# 我们先看map，map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
r = map(f, l1)
print(isinstance(r, Iterator))
print(isinstance(r, Iterable))
print(isinstance(r, map))
print(type(r))

# 把这个list所有数字转为字符串：
print(list(map(str, l1)))
print('==================reduce====================')

from functools import reduce

add = lambda x, y: x + y

l2 = list(range(1, 5))

r = reduce(add, l2)

print(r)

# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

fn = lambda x, y: x * 10 + y

print(reduce(fn, l2))
