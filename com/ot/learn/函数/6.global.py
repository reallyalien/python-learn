# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"


def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd = "http://c.biancheng.net/shell/"


var = globals()
var['Shename'] = 'aaaaaaaaaaaaaaaaa'
# dict
print(var)
print(type(var))
