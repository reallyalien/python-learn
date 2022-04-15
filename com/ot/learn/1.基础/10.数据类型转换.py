# 浮点型和字符串不能直接连，需要数据类型转换
height = 178.0
print("a" + str(height))
'''
int(x)	将 x 转换成整数类型
float(x)	将 x 转换成浮点数类型
complex(real，[,imag])	创建一个复数
str(x)	将 x 转换为字符串   将值转化为适于人阅读的字符串的形式
repr(x)	将 x 转换为表达式字符串    将值转化为供解释器读取的字符串形式
eval(str)	计算在字符串中的有效 Python 表达式，并返回一个对象
chr(x)	将整数 x 转换为一个字符
ord(x)	将一个字符 x 转换为它对应的整数值 
hex(x)	将一个整数 x 转换为一个十六进制字符串
oct(x)	将一个整数 x 转换为一个八进制的字符串
'''

print(str(1))

print('=======================')
print(ord('C'))
print(ord('A'))
print(chr(65))

print('=======================')
print(hex(11))
print(oct(2))
print(bin(10))

'''
1.除了字符串类型外，使用str还是repr转换没有什么区别，字符串类型的话，外层会多一对引号，这一特性有时候在eval操作时特别有用；

2.命令行下直接输出对象调用的是对象的repr方法，print输出调用的是str方法
'''

print('===================')
str1 = 'hello'

print(repr(str1))
print(str(str1))
print(len(repr(str1)))
print(len(str(str1)))

# repr的使用场景
s = 'abdcf'
# python的join方法与java相反
print(eval('[' + ','.join([repr(i) for i in s]) + ']'))
