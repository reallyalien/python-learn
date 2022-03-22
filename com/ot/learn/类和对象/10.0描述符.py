'''
1.每个对象都有__dict__属性

对象属性的访问顺序：

①.实例属性

②.类属性

③.父类属性

④.__getattr__()方法
'''


class Test(object):
    cls_val = 1

    def __init__(self):
        self.ins_val = 10


t = Test()
for item in Test.__dict__:
    print(item)
print("t==============================")
print(t.__dict__)

print("============================================描述符正式开始")

'''
　问题1. 为什么访问 t.x的时候，会直接去调用描述符的 __get__() 方法呢？

　　　　答：t为实例，访问t.x时，根据常规顺序，

　　　　　　首先：访问Owner的__getattribute__()方法（其实就是 TestDesc.__getattribute__())，访问实例属性，发现没有，然后去访问父类TestDesc，找到了！

　　　　　　其次：判断属性 x 为一个描述符，此时，它就会做一些变动了，将 TestDesc.x 转化为 TestDesc.__dict__['x'].__get__(None, TestDesc) 来访问

　　　　　　然后：进入类Desc的 __get__()方法，进行相应的操作
'''


class Desc(object):

    def __get__(self, instance, owner):
        print("__get__...")
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("owner : \t", owner)
        print('=' * 40, "\n")

    def __set__(self, instance, value):
        print('__set__...')
        print("self : \t\t", self)
        print("instance : \t", instance)
        print("value : \t", value)
        print('=' * 40, "\n")


class TestDesc(object):
    x = Desc()


t = TestDesc()
print(t.x)
print(TestDesc.__dict__['x'].__get__(None, TestDesc))
