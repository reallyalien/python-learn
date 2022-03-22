class Person:
    def __init__(self):
        print("正在执行构造方法")

    # 定义一个study()实例方法
    def study(self):
        print(self, "正在学Python")


# 也就是说，同一个类可以产生多个对象，当某个对象调用类方法时，该对象会把自身的引用作为第一个参数自动传给该方法，换句话说，
# Python 会自动绑定类方法的第一个参数指向调用该方法的对象。如此，Python解释器就能知道到底要操作哪个对象的方法了。

zhangsan = Person()
lisi = Person()

zhangsan.study()
lisi.study()
