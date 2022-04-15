class MyText(object):
    work = '刺客'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print('my name is {}'.format(self.name))


print(type(MyText))
