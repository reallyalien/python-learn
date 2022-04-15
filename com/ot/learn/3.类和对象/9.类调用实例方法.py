class CLanguage:
    def info(self):
        print(self, "我正在学 Python")


clang = CLanguage()
# 通过类名直接调用实例方法
CLanguage.info(clang)
# 值得一提的是，上面的报错信息只是让我们手动为 self 参数传值，但并没有规定必须传一个该类的对象，其实完全可以任意传入一个参数，例如：
CLanguage.info("zaaaaaaaaaaaaaa")

# 用类的实例对象访问类成员的方式称为绑定方法，而用类名调用类成员的方式称为非绑定方法。