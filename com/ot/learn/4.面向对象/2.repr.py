class Encouragement:

    def __init__(self):
        self.name = "c"
        self.age = "10"

    def __repr__(self):
        return "Encouragement[name=" + self.name + ",age=" + self.age + "]"


e = Encouragement()
print(Encouragement)
print(e)
print('-----------------')
print(type(Encouragement))
print(type(e))
print(e.__repr__())

str = "时间你好"
print(str)
