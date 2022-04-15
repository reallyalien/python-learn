# 系统自带模块
# import datetime
from datetime import datetime

print(type(datetime))  # <class 'module'>


def _cmp(x, y):
    return 0 if x == y else (1 if x > y else -1)


print(_cmp(1, 0))
