# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 0 1 1 2 3 5 8 13
class FIb(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        # 实例本身就是迭代器，故返回自身
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100000:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item + 1):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            if start is None:
                start = 0

            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L


f = FIb()
# for x in f:
#     print(x)

# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：f[5] ,要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
print(f[0])
print(f[1])
print(f[2])
print(f[3])
print(f[4])
print(f[1:2])
# 但是list有个神奇的切片方法：list[0:2],对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：

s = slice(1, 2, 3)
print(s)
