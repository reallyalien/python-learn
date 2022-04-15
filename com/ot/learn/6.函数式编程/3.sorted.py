print(sorted([1, -23, 89, 100, 45], key=abs))

print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def process(t):
    return t[0]


# 按名字排序
print(sorted(L, key=lambda x: x[0]))

# 按成绩从高到低
print(sorted(L, key=lambda x: x[1], reverse=True))

print(sum([1, 2, 3]))
