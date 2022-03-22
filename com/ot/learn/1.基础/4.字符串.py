print("I' am a  boy ")

print("aaaaaaaaaaaaaaaaaaaaa\
      aaaaaaaaaaaaaaaaaa")

# 长字符串 在三个单引号中间的内容会原样输出，包括空白符，换行符
longstr = '''It took me 6 months to write this Python tutorial.
Please give me a to 'thumb' to keep it updated.
The Python tutorial is available at http://c.biancheng.net/python/.'''
print(longstr)

print('''------------------------------''')

longstr = '''
    It took me 6 months to write this Python tutorial.
    Please give me a to 'thumb' to keep it updated.
    The Python tutorial is available at http://c.biancheng.net/python/.
'''
print(longstr)

# python的原始字符串 \不表示转义,在普通字符串的前面加上‘r’。就表示原始字符串,
# 需要注意的是，Python 原始字符串中的反斜杠仍然会对引号进行转义，因此原始字符串的结尾处不能是反斜杠，否则字符串结尾处的引号会被转义，导致字符串不能正确结束。
rstr = r"D:\Program Files\Python 3.8\python.exe"
print(rstr)

rstr = r"D:\Program Files\Python 3.8\python.exe""\\"
print(rstr)

print(type(str(1)))

str1 = "a'b"

print(str1)
