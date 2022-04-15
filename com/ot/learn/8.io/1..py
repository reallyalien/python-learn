try:
    f = open('/home/wangtao/baidu/1.txt', 'r', encoding='utf-8')
    print(f)
    print(type(f))

    s = f.read()

    print(s)
finally:
    if f:
        f.close()

# with语法等同于上述，而且还不需要手动关闭流
with open('/home/wangtao/baidu/1.txt', 'r') as f:
    print(f.read())

# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，每次最多读取size个字节的内容。
# 另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
# 如果文件很小，read()一次性读取最方便；
# 如果不能确定文件大小，反复调用read(size)比较保险；
# 如果是配置文件，调用readlines()最方便：

# file-like Object
# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
# StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
