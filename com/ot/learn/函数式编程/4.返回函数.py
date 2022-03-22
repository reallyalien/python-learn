def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


def lazy_calc_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax

    return sum


# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，
# 当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：


f = lazy_calc_sum(1, 2, 3)
print(f())
