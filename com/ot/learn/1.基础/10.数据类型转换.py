# 浮点型和字符串不能直接连，需要数据类型转换
height = 178.0
print("a" + str(height))
'''
int(x)	将 x 转换成整数类型
float(x)	将 x 转换成浮点数类型
complex(real，[,imag])	创建一个复数
str(x)	将 x 转换为字符串
repr(x)	将 x 转换为表达式字符串
eval(str)	计算在字符串中的有效 Python 表达式，并返回一个对象
chr(x)	将整数 x 转换为一个字符
ord(x)	将一个字符 x 转换为它对应的整数值 
hex(x)	将一个整数 x 转换为一个十六进制字符串
oct(x)	将一个整数 x 转换为一个八进制的字符串
'''

print(str(1))

print(ord('C'))
print(ord('A'))
print(chr(65))

print(hex(11))
print(oct(2))
print(bin(10))
