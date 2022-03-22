# 二进制文件
# 前面讲的默认都是读取文本文件，并且是UTF-8编码的文本文件。要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：

with open('/home/wangtao/baidu/倒计时为0.点击支付，提示服务异常.mp4', 'rb') as f:
    print(f.read())
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
#
# >>> f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：


with open('/home/wangtao/baidu/1.txt', 'a',) as f:
    f.write('hello 中国')
