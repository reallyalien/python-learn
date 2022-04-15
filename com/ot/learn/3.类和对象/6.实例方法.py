'''
和类属性一样，类方法也可以进行更细致的划分，具体可分为类方法、实例方法和静态方法。

和类属性的分类不同，对于初学者来说，区分这 3 种类方法是非常简单的，即
采用 @classmethod 修饰的方法为类方法；
采用 @staticmethod 修饰的方法为静态方法；
不用任何修改的方法为实例方法。

'''


class People:

    def __init__(self):
        print("构造方法执行了")

    # 实例方法最大的特点就是，它最少也要包含一个 self 参数，用于绑定调用此方法的实例对象（Python 会自动完成绑定）。实例方法通常会用类对象直接调用，例如：
    def say(self, name):
        print(name)


a = People()
a.say("a")

# 当然，Python 也支持使用类名调用实例方法，但此方式需要手动给 self 参数传值。例如：
People.say(a, "aaaaaaaaa")
