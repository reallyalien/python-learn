class Clanguage:
    def say(self):
        print("调用的是 Clanguage 类的say方法")


class CPython(Clanguage):
    def say(self):
        print("调用的是 CPython 类的say方法")


class CLinux(Clanguage):
    def say(self):
        print("调用的是 CLinux 类的say方法")


a = Clanguage()
a.say()

a = CPython()
a.say()

a = CLinux()
a.say()

print(
    '==========================================================================================================================')


class WhoSay:
    def say(self, who):
        who.say()


class CLanguage:
    def say(self):
        print("调用的是 Clanguage 类的say方法")


class CPython(CLanguage):
    def say(self):
        print("调用的是 CPython 类的say方法")


class CLinux(CLanguage):
    def say(self):
        print("调用的是 CLinux 类的say方法")


b = WhoSay()
b.say(Clanguage())
b.say(CPython())
b.say(CLinux())
