def calculate(*numbers):
    # print(type(numbers)) tuple
    sum = 0
    for x in numbers:
        sum += x * x
    return sum


print(calculate(1, 2, 3))

# 如果已经有一个list或者tuple
l1 = [1, 2, 3]
t1 = (1, 2, 3)
# *将l1作为可变参传入函数
print(calculate(*l1))
print(calculate(*t1))
