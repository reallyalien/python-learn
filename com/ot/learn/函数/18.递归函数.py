def fact(x):
    if x == 1:
        return 1
    return fact(x - 1) * x


print(fact(1))
print(fact(2))
print(fact(3))

# print(fact(1000))

print('=========================================')
count1 = 0


def move(n, a, b, c):
    global count1
    count1 = count1 + 1
    if n == 1:
        pass
    else:
        move(n - 1, a, c, b)
        move(n - 1, b, a, c)


move(20, 'a', 'b', 'c')
print(count1)
