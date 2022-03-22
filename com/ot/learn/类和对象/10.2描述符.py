class Desc(object):
    def __init__(self, name):
        self.name = name
        print("__init__(): name = ", self.name)

    def __get__(self, instance, owner):
        print("__get__() ...")
        return self.name

    # 将set方法注释之后，就是非描述符，对于实例对象t来讲，实例属性的优先级大于非数据描述符
    # def __set__(self, instance, value):
    #     self.value = value


class TestDesc(object):
    _x = Desc('x')

    def __init__(self, x):
        self._x = x


t = TestDesc(x=1)
t._x
'''
问题3. 如果 类属性的描述符对象 和 实例属性描述符的对象 同名时，咋整？
　不对啊，按照惯例，t._x 会去调用 __getattribute__() 方法，然后找到了 实例t 的 _x 属性就结束了，为啥还去调用了描述符的 __get__() 方法呢？

　　　　这就牵扯到了一个查找顺序问题：当Python解释器发现实例对象的字典中，有与描述符同名的属性时，描述符优先，会覆盖掉实例属性。
'''
print(t.__dict__)
print(TestDesc.__dict__)
# print(TestDesc.__getattribute__())

'''
　问题5. 天天提属性查询优先级，就不能总结一下吗？

　　　　答：好的好的，客官稍等！

　　　　① __getattribute__()， 无条件调用

　　　　② 数据描述符：由 ① 触发调用 （若人为的重载了该 __getattribute__() 方法，可能会调职无法调用描述符）

　　　　③ 实例对象的字典（若与描述符对象同名，会被覆盖哦）

　　　　④ 类的字典

　　　　⑤ 非数据描述符

　　　　⑥ 父类的字典

　　　　⑦ __getattr__() 方法

 


'''
'''
为什么会这个结果呢？
__getattribute__是属性访问拦截器，就是当这个类的属性被访问时，会自动调用类的__getattribute__方法。即在上面代码中，当我调用实例对象aa的name属性时，
不会直接打印，而是把name的值作为实参传进__getattribute__方法中（参数obj是我随便定义的，可任意起名），经过一系列操作后，再把name的值返回。
Python中只要定义了继承object的类，就默认存在属性拦截器，只不过是拦截后没有进行任何操作，而是直接返回。所以我们可以自己改写__getattribute__方法来实现相关功能，
比如查看权限、打印log日志等。如下代码，简单理解即可：
'''


class Tree(object):
    def __init__(self, name):
        self.name = name
        self.cate = "plant"

    def __getattribute__(self, item):
        if item == 'name':
            return "I love 大树"
        else:
            return object.__getattribute__(self, item)

        # def __getattribute__(self, *args, **kwargs):
        #     if args[0] == "大树":
        #         print("log 大树")
        #         return "我爱大树"
        #     else:
        #         return object.__getattribute__(self, *args, **kwargs)


aa = Tree("大树")
print(aa.name)
print(aa.cate)
