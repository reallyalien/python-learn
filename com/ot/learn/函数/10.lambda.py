# 对于定义一个简单的函数，Python 还提供了另外一种方法，即使用本节介绍的 lambda 表达式。
# lambda 表达式，又称匿名函数，常用来表示内部仅包含 1 行表达式的函数。如果一个函数的函数体仅有 1 行表达式，
# 则该函数就可以用 lambda 表达式来代替。

def add(x, y):
    return x + y


print(add(1, 2))
# 可以这样理解 lambda 表达式，其就是简单函数（函数体仅是单行的表达式）的简写版本。相比函数，lambda 表达式具有以下  2 个优势：
# 对于单行函数，使用 lambda 表达式可以省去定义函数的过程，让代码更加简洁；
# 对于不需要多次复用的函数，使用 lambda 表达式可以在用完之后立即释放，提高程序执行的性能。
# lambda

multi = lambda x, y: x * y
add1 = lambda a, b, c: a + b + c
print(multi(1, 10))
print(add1(1, 2, 3))
