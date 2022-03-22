import os

print(os.name)
print(os.uname())

# 环境变量
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：

print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：

print(os.environ.get('HOME'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径
print(os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
print(os.path.join('/home/wangtao/python/project/learn/com/ot/learn', 'testdir'))
# 然后创建一个目录:
# os.mkdir('/home/wangtao/python/project/learn/com/ot/learn/testdir')
# 删除一个目录
# os.rmdir('/home/wangtao/python/project/learn/com/ot/learn/testdir')

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
#
# part-1/part-2
# 而Windows下会返回这样的字符串：
#
# part-1\part-2
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
#
# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')


# print(os.path.split('/Users/michael/testdir'))
print(os.path.splitext('/Users/michael/testdir.txt'))

# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。


# 对文件进行重命名
# os.rename('/home/wangtao/python/project/learn/com/ot/learn/1.txt',
#           '/home/wangtao/python/project/learn/com/ot/learn/2.txt')

# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。

# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
print('---------------------------------')
print(x for x in os.listdir('.') if os.path.isdir(x))
