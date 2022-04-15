class Cat:
    def __init__(self):
        print('构造方法')


zs = Cat()
zs.money = "aaa"
del zs.money


# print(zs.money)


# 需要注意的一点是，为 clanguage 对象动态增加的方法，Python 不会自动将调用者自动绑定到第一个参数（即使将第一个参数命名为 self 也没用）。例如如下代码：
# 非绑定方法
# 需要手动给self传参

def info(self):
    print("--info function--", self)


# zs.foo = info
# zs.foo()
# # 手动将调用者绑定到第一个参数
# zs.foo(zs)

# 通过借助 types 模块下的 MethodType 可以实现，仍以上面的 info() 函数为例：

from types import MethodType

# 将info绑定到zs对象上面,第一个参数是实例要绑定的方法，第二个参数是实例，第三参数是类()
zs.info = MethodType(info, zs)
# zs.info = info

zs.info()
