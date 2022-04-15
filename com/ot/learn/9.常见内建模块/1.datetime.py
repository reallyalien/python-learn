# datetime是Python处理日期和时间的标准库。

from datetime import datetime, timedelta

now = datetime.now()

print(now)
print(type(now))

# dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime

dt = datetime(2015, 4, 19, 12, 20)
print(dt)

# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：
# 注意Python的timestamp是一个浮点数，整数位表示秒。
print(dt.timestamp())

# timestamp转换成dateTime


# 字符串转datetime 实例调用也可以，通过类名调用也可以
# d = datetime.strftime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
d = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
e = now.strftime('%Y-%m-%d %H:%M:%S')
f = datetime.strftime(now, '%Y-%m-%d %H:%M:%S')
print('-----------------------d e f')
print(d)
print(e)
print(f)

# datetime加减
# 对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：

y = now - timedelta(hours=-12)
y = now - timedelta(days=12)

print(y)
z = y.strftime('%Y-%m-%d %H:%M:%S')
print(type(y))
print(z)
print(type(z))
