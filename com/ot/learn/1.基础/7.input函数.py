"""
input() 是 Python 的内置函数，用于从控制台读取用户输入的内容。input() 函数总是以字符串的形式来处理用户输入的内容，所以用户输入的内容可以包含任何字符。
"""

a = input("Enter a number: ")
b = input("Enter another number: ")
print("aType: ", type(a))
print("bType: ", type(b))
result = int(a) + int(b)
print("resultValue: ", result)
print("resultType: ", type(result))
'''
我们可以使用 Python 内置函数将字符串转换成想要的类型，比如：
int(string) 将字符串转换成 int 类型；
float(string) 将字符串转换成 float 类型；
bool(string) 将字符串转换成 bool 类型。

'''