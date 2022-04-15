print(dir(dict))

scores = {'数学': 95, '语文': 89, '英语': 90}
print(scores.keys())
print(scores.values())
print(scores.items())
print(type(scores.keys()))
print(type(scores.values()))
print(type(scores.items()))
'''
可以发现，keys()、values() 和 items() 返回值的类型分别为 dict_keys、dict_values 和 dict_items。

需要注意的是，在 Python 2.x 中，上面三个方法的返回值都是列表（list）类型。但在 Python 3.x 中，它们的返回值并不是我们常见的列表或者元组类型，
因为 Python 3.x 不希望用户直接操作这几个方法的返回值。
'''

print(list(scores.keys()))
print(list(scores.items()))

# for循环遍历
print("======================================================================")
a = {'数学': 95, '语文': 89, '英语': 90}
for k in a.keys():
    print(k, end=' ')
print("\n---------------")
for v in a.values():
    print(v, end=' ')
print("\n---------------")
for k, v in a.items():
    print("key:", k, " value:", v)
'''
a = {'one': 1, 'two': 2, 'three': [1,2,3]}
b = a.copy()
print(b)
注意，copy() 方法所遵循的拷贝原理，既有深拷贝，也有浅拷贝。拿拷贝字典 a 为例，copy() 方法只会对最表层的键值对进行深拷贝，
也就是说，它会再申请一块内存用来存放 {'one': 1, 'two': 2, 'three': []}；而对于某些列表类型的值来说，此方法对其做的是浅拷贝，
也就是说，b 中的 [1,2,3] 的值不是自己独有，而是和 a 共有。
'''
print("copy========================================================================")

a = {'one': 1, 'two': 2, 'three': [1, 2, 3]}
b = a.copy()
print(a)
a['three'].append(1)
print(a)
print(b)

'''
update() 方法可以使用一个字典所包含的键值对来更新己有的字典。

在执行 update() 方法时，如果被更新的字典中己包含对应的键值对，那么原 value 会被覆盖；如果被更新的字典中不包含对应的键值对，则该键值对被添加进去。
'''
print("update========================================================================")
a = {'one': 1, 'two': 2, 'three': 3}
a.update({'one': 4.5, 'four': 9.3})
print(a)
a['one'] = 111111
print(a)

'''
pop() 和 popitem() 都用来删除字典中的键值对，不同的是，pop() 用来删除指定的键值对，而 popitem() 用来随机删除一个键值对(删除最后一个元素)，它们的语法格式如下：
'''
print('pop=============================================================')
a = {'数学': 95, '语文': 89, '英语': 90, '化学': 83, '生物': 98, '物理': 89}
print(a)
a.pop('化学')
print(a)
a.popitem()
print(a)

a.setdefault("数学1")
print(a)
