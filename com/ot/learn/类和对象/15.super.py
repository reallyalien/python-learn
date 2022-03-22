class People:
    def __init__(self, name):
        self.name = name

    def say(self):
        print("我是人，名字为：", self.name)


class Animal:
    def __init__(self, food):
        self.food = food

    def display(self):
        print("我是动物,我吃", self.food)


class Person(People, Animal):
    def __init__(self, name, food):
        # 子类的构造方法当中必须调用父类的构造方法
        # 使用super()函数->调用 People 类的构造方法
        super().__init__(name)
        # super只能调用第一个直接父类的构造方法,因此要调用第二个父类的构造方法，只能使用非绑定方法来调用
        Animal.__init__(self, food)


a = Person("aaaaaaa", "熟食")
a.say()
a.display()

'''
针对这种情况，正确的做法是定义 Person 类自己的构造方法（等同于重写第一个直接父类的构造方法）。
但需要注意，如果在子类中定义构造方法，则必须在该方法中调用父类的构造方法。

在子类中的构造方法中，调用父类构造方法的方式有 2 种，分别是：
1.类可以看做一个独立空间，在类的外部调用其中的实例方法，可以向调用普通函数那样，只不过需要额外备注类名（此方式又称为未绑定方法）；
2.使用 super() 函数。但如果涉及多继承，该函数只能调用第一个直接父类的构造方法。
也就是说，涉及到多继承时，在子类构造函数中，调用第一个父类构造方法的方式有以上 2 种，而调用其它父类构造方法的方式只能使用未绑定方法。
'''
