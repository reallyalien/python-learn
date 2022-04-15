# 那么，如何判断一个对象是可迭代对象呢？方法是通过collections.abc模块的Iterable类型判断：

from collections.abc import Iterable

print(isinstance('abc', Iterable))
print(isinstance([1, 2], Iterable))
print(isinstance((1, 2), Iterable))

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：

l1 = [1, 2, 3]
for i, v in enumerate(l1):
    print(i, v)

for i, v in enumerate('abc'):
    print(i, v)
