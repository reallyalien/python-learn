import functools


def now():
    print('2022-03-04')


f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字：

print(f.__name__)

# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：

print('-------------------------------------------------------')


def log(f):
    @functools.wraps(f)
    # wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用
    def wrapper(*args, **kwargs):
        print('call %s():' % f.__name__)
        return f(*args, **kwargs)

    return wrapper


@log
def now():
    print('2022-03-04')


now()
# 把@log放到now()函数的定义处，相当于执行了语句： now=log(now)

now = log(now)
print(now.__name__)
print('---------------------------------------------------------')


# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log(text):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            print('%s %s():' % (text, f.__name__))
            return f(*args, **kwargs)

        return wrapper

    return decorator


@log('execute')
def now():
    print('2015-3-25')


now()

now = log("aaaa")(now)
print(now.__name__)

# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，
# 但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：


# import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。
