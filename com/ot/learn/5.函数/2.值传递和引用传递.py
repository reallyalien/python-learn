'''

Python 中，根据实际参数的类型不同，函数参数的传递方式可分为 2 种，分别为值传递和引用（地址）传递：
1.值传递：适用于实参类型为不可变类型（字符串、数字、元组）；
2.引用（地址）传递：适用于实参类型为可变类型（列表，字典）；
与java一样，可以理解为值传递，引用传递传递的是引用对象的地址值

'''


def demo(obj):
    obj += obj
    return obj


print("基础类型======================================")
a = 100
a1 = demo(a)
print(a)
print(a1)
print(a)
print("字符串======================================")
b = "hello"
b1 = demo(b)
print(b)
print(b1)
print(b)
print("元组======================================")
c = (1, 2)
c1 = demo(c)
print(c)
print(c1)
print(c)
print("list======================================")
d = [1, 2]
d1 = demo(d)
print(d)
print(d1)
print(d)
print(d is d1)
'''
查看python内置函数的默认值
'''
print(demo.__defaults__)
