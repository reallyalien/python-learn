# 闭包，又称闭包函数或者闭合函数，其实和前面讲的嵌套函数类似，不同之处在于，
# 闭包中外部函数返回的不是一个具体的值，而是一个函数。一般情况下，返回的函数会赋值给一个变量，这个变量可以在后面被继续执行调用。

# 闭包函数，其中 exponent 称为自由变量
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of  # 返回值是 exponent_of 5.函数


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方
print(square(2))  # 计算 2 的平方
print(cube(2))  # 计算 2 的立方
# 闭包比普通的函数多了一个 __closure__ 属性，该属性记录着自由变量的地址。当闭包被调用时，系统就会根据该地址找到对应的自由变量，完成整体的函数调用。
# 以 nth_power() 为例，当其被调用时，可以通过 __closure__ 属性获取自由变量（也就是程序中的 exponent 参数）存储的地址，例如：
# 还可以看到，__closure__ 属性的类型是一个元组，这表明闭包可以支持多个自由变量的形式。
a = square.__closure__

print(type(a))
