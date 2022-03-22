# 只要写成指数形式就是小数，尽管最后还是整数,python只有一种小数类型，float类型，小数在计算机存储的时候是二进制，可能会出现无限不循环，小数表示不精确
print(type(2E2))
print('==========================')
f1 = 12.5
print("f1Value: ", f1)
print("f1Type: ", type(f1))
f2 = 0.34557808421257003
print("f2Value: ", f2)
print("f2Type: ", type(f2))
f3 = 0.0000000000000000000000000847
print("f3Value: ", f3)
print("f3Type: ", type(f3))
f4 = 345679745132456787324523453.45006
print("f4Value: ", f4)
print("f4Type: ", type(f4))
f5 = 12e4
print("f5Value: ", f5)
print("f5Type: ", type(f5))
f6 = 12.3 * 0.1
print("f6Value: ", f6)
print("f6Type: ", type(f6))

