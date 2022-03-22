'''
值得一提的是，布尔类型可以当做整数来对待，即 True 相当于整数值 1，False 相当于整数值 0。因此，下边这些运算都是可以的：
'''

print(True + 1)
print(False + 1)
'''
注意，这里只是为了说明 True 和 Flase 对应的整型值，在实际应用中是不妥的，不要这么用。

总的来说，bool 类型就是用于代表某个事情的真（对）或假（错），如果这个事情是正确的，用 True（或 1）代表；如果这个事情是错误的，用 False（或 0）代表。
'''
print(type(1))
print(type(True))
print(type(1.0))
print(type(1 + 2j))
print(complex(1))
