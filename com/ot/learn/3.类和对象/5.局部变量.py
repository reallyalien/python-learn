class People:
    def count(self, money):
        sale = 0.8 * money
        print("优惠后的价格为：", sale)


a = People()
a.count(100)

# 通常情况下，定义局部变量是为了所在类方法功能的实现。需要注意的一点是，局部变量只能用于所在函数中，函数执行完成后，局部变量也会被销毁。
