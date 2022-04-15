# zip() 函数是 Python 内置函数之一，它可以将多个序列（列表、元组、字典、集合、字符串以及 range() 区间构成的列表）
# “压缩”成一个 zip 对象。所谓“压缩”，其实就是将这些序列中对应位置的元素重新组合，生成一个个新的元组。

my_list = [11, 12, 13]
my_tuple = (21, 22, 23)

for x in zip(my_list, my_tuple):
    print(x)
print(type(zip(my_list, my_tuple)))
print([x for x in zip(my_list, my_tuple)])
print(zip(my_list, my_tuple))

my_dic = {31: 2, 32: 4, 33: 5}
my_set = {41, 42, 43, 44, 44}
print("----------------------------------------------------------------------------------")
print(my_set)
for x in zip(my_dic, my_set):
    print(x)
