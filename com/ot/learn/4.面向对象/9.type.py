class ListMetaClass(type):
    pass


print(type(object))  # <class 'type'>
print(type(type))  # <class 'type'>

print(type.__class__)  # <class 'type'>
print(object.__class__)  # <class 'type'>

print(object.__bases__)  # object没有父类，因它是链条的顶端
print(type.__bases__)  # object没有父类，因它是链条的顶