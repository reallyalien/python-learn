add = "http://c.biancheng.net/shell/"

def text():
    print("函数体内访问：", add)


text()
print('函数体外访问：', add)


def text():
    # 在使用 global 关键字修饰变量名时，不能直接给变量赋初值，否则会引发语法错误。
    global add1
    add1 = "http://c.biancheng.net/java/"
    print("函数体内访问：", add1)


text()
print('函数体外访问：', add1)

# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"


def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd = "http://c.biancheng.net/shell/"


var = globals()
# dict
print(var)
print(type(var))
# 2) locals()5.函数
# locals() 函数也是 Python 内置函数之一，通过调用该函数，我们可以得到一个包含当前作用域内所有变量的字典。
# 这里所谓的“当前作用域”指的是，在函数内部调用 locals() 5.函数，会获得包含所有局部变量的字典；而在全局范文内调用 locals() 5.函数，其功能和 globals() 函数相同。
