a = {"one": 1, "two": 2}
print(a)
print(type(a))

'''
通过python自带的函数创建dict,fromkeys
dictname = dict.fromkeys(list，value=None)

其中，list 参数表示字典中所有键的列表（list）；value 参数表示默认值，如果不写，则为空值 None。
一般用于设置默认值

'''
b = dict.fromkeys(['a', 'b', 'c'])
print(b)

'''
通过 dict() 函数创建字典的写法有多种，表 2 罗列出了常用的几种方式，它们创建的都是同一个字典 a。

表 2 dict() 函数创建字典
创建格式	注意事项
a = dict(str1=value1, str2=value2, str3=value3)	str 表示字符串类型的键，value 表示键对应的值。使用此方式创建字典时，字符串不能带引号。

#方式1
demo = [('two',2), ('one',1), ('three',3)]
#方式2
demo = [['two',2], ['one',1], ['three',3]]
#方式3
demo = (('two',2), ('one',1), ('three',3))
#方式4
demo = (['two',2], ['one',1], ['three',3])
a = dict(demo)	向 dict() 函数传入列表或元组，而它们中的元素又各自是包含 2 个元素的列表或元组，其中第一个元素作为键，第二个元素作为值。


keys = ['one', 'two', 'three'] #还可以是字符串或元组
values = [1, 2, 3] #还可以是字符串或元组
a = dict( zip(keys, values) )	通过应用 dict() 函数和 zip() 5.函数，可将前两个列表转换为对应的字典。

'''
print("================================================================")
a = dict(c=1, d=2)
print(a)

b = dict(zip('hjk', 'opi'))
print(b)

print(b.get('mn', '键不存在'))

'''
修改，删除，dict,

判断字典中是否存在指定键值对
如果要判断字典中是否存在指定键值对，首先应判断字典中是否有对应的键。判断字典是否包含指定键值对的键，可以使用 in 或 not in 运算符。
需要指出的是，对于 dict 而言，in 或 not in 运算符都是基于 key 来判断的。
'''

a = {'数学': 95, '语文': 89, '英语': 90}
# 判断 a 中是否包含名为'数学'的key
print('数学' in a)  # True
# 判断 a 是否包含名为'物理'的key
print('物理' in a)  # False
