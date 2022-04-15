'''
一些具有特殊含义的类，其实例化对象的个数往往是固定的，比如用一个类表示月份，则该类的实例对象最多有 12 个；再比如用一个类表示季节，则该类的实例化对象最多有 4 个。

针对这种特殊的类，Python 3.4 中新增加了 Enum 枚举类。也就是说，对于这些实例化对象个数固定的类，可以用枚举类来定义。

'''
from enum import Enum, unique


@unique
class Color(Enum):
    # 为序列值指定value值
    red = 1
    green = 2
    blue = 3


# 在 Color 枚举类中，red、green、blue 都是该类的成员（可以理解为是类变量）。
# 注意，枚举类的每个成员都由 2 部分组成，分别为 name 和 value，其中 name 属性值为该枚举值的变量名（如 red），value 代表该枚举值的序号（序号通常从 1 开始）。

# 调用枚举类当中的成员

print(Color.red)
print(Color['red'])
print(Color(1))

# 获取name或者value
print(Color.red.name)
print(Color.red.value)
# 遍历成员
for color in Color:
    print(color)

# 枚举类成员之间不能比较大小，但可以用 == 或者 is 进行比较是否相等，例如：
print(Color.red == Color.green)
print(Color.red.name is Color.green.name)
# 需要注意的是，枚举类中各个成员的值，不能在类的外部做任何修改，也就是说，下面语法的做法是错误的：
# 除此之外，该枚举类还提供了一个 __members__ 属性，该属性是一个包含枚举类中所有成员的字典，通过遍历该属性，也可以访问枚举类中的各个成员。例如：
for name, member in Color.__members__.items():
    print(name, "->", member)
print(type(Color.__members__))  # mappingproxy

print('=========================================================================================================')

# # 除了通过继承enum实现枚举类，还可以通过enum函数
Enum("Color", ('red', 'green', 'blue'))
print(Color.red.value)

# 对象的id标识
print(id(Color))
