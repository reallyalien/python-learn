from enum import Enum

# 创建一个枚举类
Color1 = Enum("Color1", ('red', 'green', 'blue'))
# 调用枚举成员的 3 种方式
print(Color1.red)
print(Color1['red'])
print(Color1(1))
# 调取枚举成员中的 value 和 name
print(Color1.red.value)
print(Color1.red.name)
# 遍历枚举类中所有成员的 2 种方式
for color in Color1:
    print(color.name,color.value)
