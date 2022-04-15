# age = int(input("请输入你的年龄："))
# if age > 10:
#     print("你还未成年，建议在家人陪同下使用该软件！")
#     print("如果你已经得到了家长的同意，请忽略以上提示。")
# # 该语句不属于if的代码块
# print("软件正在使用中...")


# import sys
#
# age = int(input("请输入你的年龄："))
# if age < 18:
#     print("警告：你还未成年，不能使用该软件！")
#     print("未成年人应该好好学习，读个好大学，报效祖国。")
#     sys.exit()
# else:
#     print("你已经成年，可以使用该软件。")
#     print("时间宝贵，请不要在该软件上浪费太多时间。")
# print("软件正在使用中...")

'''
上面说过，if 和 elif 后面的“表达式”的形式是很自由的，只要表达式有一个结果，不管这个结果是什么类型，Python 都能判断它是“真”还是“假”。

布尔类型（bool）只有两个值，分别是 True 和 False，Python 会把 True 当做“真”，把 False 当做“假”。

对于数字，Python 会把 0 和 0.0 当做“假”，把其它值当做“真”。

对于其它类型，当对象为空或者为 None 时，Python 会把它们当做“假”，其它情况当做真。比如，下面的表达式都是不成立的：
""  #空字符串
[ ]  #空列表
( )  #空元组
{ }  #空字典
None  #空值
'''
b = False
if b:
    print('b是True')
else:
    print('b是False')
n = 0
if n:
    print('n不是零值')
else:
    print('n是零值')
s = " "
if s:
    print('s不是空字符串')
else:
    print('s是空字符串')
l = []
if l:
    print('l不是空列表')
else:
    print('l是空列表')
d = {}
if d:
    print('d不是空字典')
else:
    print('d是空字典')


def func():
    print("函数被调用")


# 对于没有 return 语句的函数，返回值为空，也即 None。

if func():
    print('func()返回值不是空')
else:
    print('func()返回值为空')

