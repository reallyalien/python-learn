try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

print('=============================================')


# err.py:
def foo(s):
    return 10 / int(s)


def bar(s):
    return foo(s) * 2


def main():
    bar('0')

import logging

try:
    main()
except BaseException as e:
    logging.error(e)
finally:
    print('finally')
