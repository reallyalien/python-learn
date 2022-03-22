age = int(input("请输入你的年龄："))
if age < 12:
    print("婴幼儿")
elif 12 <= age < 18:
    print("青少年")
elif 18 <= age < 30:
    print("成年人")
elif 30 <= age < 50:
    pass
else:
    print("老年人")

#像上面的情况，有时候程序需要占一个位置，或者放一条语句，但又不希望这条语句做任何事情，此时就可以通过 pass 语句来实现。使用 pass 语句比使用注释更加优雅。
