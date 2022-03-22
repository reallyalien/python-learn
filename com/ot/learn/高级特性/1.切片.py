L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

print(L[0:3])

L1 = list(range(100))
# 取前10个数
print(L1[:10])

# 后10个数
print(L1[-10])

# 前10个数，每两个取一个
print(L1[:10:2])
# 所有数，每5个取一个：
print(L1[::5])

# 甚至什么都不写，只写[:]就可以原样复制一个list：
print(L1[:])
