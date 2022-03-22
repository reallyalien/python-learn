'''
字符串和 bytes 存在着千丝万缕的联系，我们可以通过字符串来创建 bytes 对象，或者说将字符串转换成 bytes 对象。有以下三种方法可以达到这个目的：
    1.如果字符串的内容都是 ASCII 字符，那么直接在字符串前面添加b前缀就可以转换成 bytes。
    2.bytes 是一个类，调用它的构造方法，也就是 bytes()，可以将字符串按照指定的字符集转换成 bytes；如果不指定字符集，那么默认采用 UTF-8。
    3.字符串本身有一个 encode() 方法，该方法专门用来将字符串按照指定的字符集转换成对应的字节串；如果不指定字符集，那么默认采用 UTF-8。
'''
# 通过构造函数创建bytes
b1 = bytes()

# 通过空字符串创建空 bytes
b2 = b''

# 通过b前缀将字符串转换成 bytes
b3 = b"http://c.biancheng.net/python/"
print("b3: ", b3.__repr__())
print("b3: ", b3)
print("b3-type: ", type(b3))
print(b3[2])
print(type(b3[3]))
print(b3[7:22])

import pickle
# 为 bytes() 方法指定字符集
b4 = bytes('C语言中文网8岁了', 'UTF-8')
print("b4: ", b4)
# 通过 encode() 方法将字符串转换成 bytes
b5 = "C语言中文网8岁了".encode('UTF-8')
print("b5: ", b5)
