'''
注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。

另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
'''


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f())
    return fs


f1, f2, f3 = count()
# 返回的函数引用了变量i，并非立即执行，等函数全部返回之后，i已经成了3，因此3个函数的结果都是9
# 返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# print(f1())
# print(f2())
# print(f3())
print(f1)
print(f2)
print(f3)


# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：
def count():
    def f(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
