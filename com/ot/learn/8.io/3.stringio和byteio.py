from io import StringIO

# StringIO顾名思义就是在内存中读写str。要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：
s = StringIO()
s.write('aaaaaaa')

print(s.getvalue())
# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：

f = StringIO('hello\nworld')

while 1:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

print('=================================')
# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
from io import BytesIO

f = BytesIO()
f.write('我爱中国'.encode('utf-8'))
print(f.getvalue())

print('aaa'.encode('utf-8'))
print(b'aaa')


