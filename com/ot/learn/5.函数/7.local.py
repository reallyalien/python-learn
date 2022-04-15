# 全局变量
Pyname = "Python教程"
Pyadd = "http://c.biancheng.net/python/"


def text():
    # 局部变量
    Shename = "shell教程"
    Sheadd = "http://c.biancheng.net/shell/"
    print("函数内部的 locals:")
    print(locals())
    locals()['Shename'] = 'ssssssssssssssssssss'
    print(locals())


text()
print("函数外部的 locals:")
print(locals())

# 显然，locals() 返回的局部变量组成的字典，可以用来访问变量，但无法修改变量的值。
