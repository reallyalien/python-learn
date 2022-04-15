# namedtuple
'''
我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：

# >>> p = (1, 2)
但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。

定义一个class又小题大做了，这时，namedtuple就派上了用场：

namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

这样一来，我们用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
'''

from collections import namedtuple

Point = namedtuple('point', ['x', 'y'])

print(type(Point))  # class type
p = Point(1, 2)
print(type(p))
print(isinstance(p, tuple))

# 类似的，如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
namedtuple('Circle', ['x', 'y', 'r'])

# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。

# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque

d = deque(['a', 'b', 'c'])

print(type(d))
d.append('x')
d.appendleft('y')
print(d)

# deque除了实现list的append()和pop()外，还支持appendleft()和popleft()，这样就可以非常高效地往头部添加或删除元素。
