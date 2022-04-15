arr = [1, "sdad"]
print(type(arr))

# 通过函数创建列表,将字符串转换成列表
list1 = list("111")
print(list1)
print(list1[0])

# Python删除列表

# del list1

print(list1)

# 添加元素
language = ["Python", "C++", "Java"]
birthday = [1991, 1998, 1995]
# 相当于序列相加，元素不去重
info = language + birthday
print("language =", language)
print("birthday =", birthday)
print("info =", info)

ll = ['Python', 'C++', 'Java']
# 追加元素,append和extend只能在末尾插入元素，insert可以在任意位置插入，append之后放在最后面，extend会将元素展开放置在末尾，
ll.append('php')
ll.append(['a', 'b'])
ll.extend(['c', 'd'])
ll.insert(0, 'index')
print('ll=%s' % ll)

'''
在 Python 列表中删除元素主要分为以下 3 种场景：
根据目标元素所在位置的索引进行删除，可以使用 del 关键字或者 pop() 方法；
根据元素本身的值进行删除，可使用列表（list类型）提供的 remove() 方法；
将列表中所有元素全部删除，可使用列表（list类型）提供的 clear() 方法。
'''
rm = ['a', 'b', 'c', 'd', 'e', 'b', 'b']
# del rm[0]
# remove方法只会删除第一个与指定元素相同的元素，如果不存在，则抛异常,因此删除之前最好判断一下元素是否存在
# if 'f' in rm:
# rm.remove('f')
# pop方法如果不写索引，则类似于出栈操作，会删除最后一个元素
# rm.pop()
rm.pop(1)
rm.clear()
print("rm=%s" % rm)

'''
修改元素的值只需要对指定索引的元素赋值即可，Python 支持通过切片语法给一组元素赋值。在进行这种操作时，如果不指定步长（step 参数），
Python 就不要求新赋值的元素个数与原来的元素个数相同；这意味，该操作既可以为列表添加元素，也可以为列表删除元素。
'''
nums = [40, 36, 89, 2, 36, 100, 7]
nums[1:4] = [-77, -52, 999]
print("nums=%s" % nums)

nums = [40, 36, 89, 2, 36, 100, 7]
# 对空切分赋值，在4个位置插入元素，
print("==================================")
nums[4: 4] = [-77, -52.5, 999]
nums[0:0] = [1, 2, 3]
print("nums=%s" % nums)

print('====================赋值单个元素')
# 使用切片语法赋值时，不支持赋值单个元素，但如果单赋值一个字符串，会将字符串当成序列进行赋值
nums[0:0] = "1"

print("nums=%s" % nums)

nums = [40, 36, 89, 2, 36, 100, 7]
# 步长为2，为第1、3、5个元素赋值
nums[1: 6: 2] = [0.025, -99, 20.5]
print("nums=%s" % nums)

'''
查找元素
'''
print("查找元素=================================")
nums = [40, 36, 89, 2, 36, 100, 7, -20.5, -999]
# 检索列表中的所有元素
print(nums.index(2))
# 检索3~7之间的元素
print(nums.index(100, 3, 7))
# 检索4之后的元素
# print(nums.index(7, 4))
# 检索一个不存在的元素
# print(nums.index(55))

nums = [40, 36, 89, 2, 36, 100, 7, -20.5, 36]
# 统计元素出现的次数
print("36出现了%d次" % nums.count(36))
print("100出现了%d次" % nums.count(100))
# 判断一个元素是否存在
if nums.count(100):
    print("列表中存在100这个元素")
else:
    print("列表中不存在100这个元素")

if 0:
    print("0")
else:
    print("1")
