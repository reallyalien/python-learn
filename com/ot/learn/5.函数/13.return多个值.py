import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


PI = math.pi
a = move(100, 100, 60, PI)
x, y = move(100, 100, 60, PI)
print(x, y)
# 返回多个值其实就是返回一个元祖，
print(type(a))
