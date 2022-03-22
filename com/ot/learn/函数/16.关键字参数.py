'''
关键字参数
可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。请看示例：

'''


def person(name, age, **kwargs):
    print('name', name, 'age', age, 'other', kwargs, type(kwargs))


person('a', 10, city='北京', age1=10)

dict1 = dict(city='上海', hello='world')
# 可变参是拷贝了一份，对内部参数的改变不会影响外层的参数
person('a', 20, **dict1)

