def log(f):
    def wrapper(*args, **kwargs):
        print('打印日志')
        return f(*args, **kwargs)

    return wrapper


def log1(text):
    def decorator(f):
        def wrapper(*args, **kwargs):
            print("打印日志 %s" % text)
            return f(*args, **kwargs)

        return wrapper

    return decorator


@log1('111')
def f():
    print('输出')


# f()

# t = log1(1)(f)()

# print(t)
