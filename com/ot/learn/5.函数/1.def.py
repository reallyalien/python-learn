def str_max(str1, str2):
    '''
    比较2个字符串的大小

    :param str1: a
    :param str2: b
    :return:
    '''
    return str1 if str1 > str2 else str2


print(str_max.__doc__)
print("-----------------------------------------")
print(help(str_max))
''

'''
前面章节讲过，通过调用 Python 的 help() 内置函数或者 __doc__ 属性，我们可以查看某个函数的使用说明文档。事实上，无论是 Python 提供给我们的函数，还是自定义的函数，
其说明文档都需要设计该函数的程序员自己编写。
其实，函数的说明文档，本质就是一段字符串，只不过作为说明文档，字符串的放置位置是有讲究的，函数的说明文档通常位于函数内部、所有代码的最前面。
'''
