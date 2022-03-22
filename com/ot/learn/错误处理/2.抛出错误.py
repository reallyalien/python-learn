class FooError(ValueError):
    pass


def foo(s):
    n = int(s)
    if n == 0:
        # raise如果不带参数，会将捕获的异常原样抛出
        raise FooError('invalid value: %s' % s)
    return 10 / n


foo('1')
