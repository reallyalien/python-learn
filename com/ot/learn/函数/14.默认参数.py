def power(a, x=2):
    return a ** x


print(power(6))


def add(l=[]):
    l.append('end')
    return l


print(add())
print(add())
print(add())


# 第一次调用，变量l指向了[]，第一次方法被调用之后。[]当中已经有一个值了，当第二次调用的时候入参其实已经成了['end']，因此要想作为默认参数，一定要是不可变参数，

def add1(l=None):
    if l == None:
        l = []
    l.append("end")
    return l


print(add1())
print(add1())
print(add1())
