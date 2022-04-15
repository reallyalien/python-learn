add = "http://c.biancheng.net/python/"
for item in add:
    print(item, end="-")

print("=======================")

result = 0
for i in range(5):
    result += i
print(result)
# range(5) 生成 1 2 3 4

print(type(range(5))) #type range


tuple1 = ('a', 'b', 'c')

for i in tuple1:
    print(i)

print("===============")

dict1 = {'a': 1, 'b': 2, 'c': 3}

for i in dict1.items():
    print(type(i))
