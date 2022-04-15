# defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：


from collections import defaultdict, OrderedDict

d = defaultdict(lambda: 'N/A')

d['key'] = 'abc'
print(isinstance(d, dict))
print('====================')
print(d['key'])
print(d['key1'])

# OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#
# 如果要保持Key的顺序，可以用OrderedDict：
d = dict([('a', 1), ('c', 2), ('b', 3)])

print(d.keys())

o = OrderedDict([('a', 1), ('c', 2), ('b', 3)])
print(o.keys())

'''
ChainMap
ChainMap可以把一组dict串起来并组成一个逻辑上的dict。ChainMap本身也是一个dict，但是查找的时候，会按照顺序在内部的dict依次查找。

什么时候使用ChainMap最合适？举个例子：应用程序往往都需要传入参数，参数可以通过命令行传入，可以通过环境变量传入，还可以有默认参数。我们可以用ChainMap实现参数的优先级查找，即先查命令行参数，如果没有传入，再查环境变量，如果没有，就使用默认参数。

下面的代码演示了如何查找user和color这两个参数：

'''

from collections import ChainMap
import os, argparse

# 构造缺省参数:
defaults = {
    'color': 'red',
    'user': 'guest'
}
p = argparse.ArgumentParser()
p.add_argument('-u', '--user')
p.add_argument('-c', '--color')

print(p)

# Counter
# Counter是一个简单的计数器，例如，统计字符出现的个数：

from collections import Counter

c = Counter()
# print(c[1]) 默认是0
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)

c.update('hello')  # 也可以一次性update

print(c)
