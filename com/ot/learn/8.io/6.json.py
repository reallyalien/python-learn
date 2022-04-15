# JSON类型	Python类型
# {}	       dict
# []	       list
# "string"	   str
# 1234.56	   int或float
# true/false   True/False
# null	       None

import json

d = {'name': 'jack', 'age': 10}
j = json.dumps(d)

print(type(j))
print(j)
dj = json.loads(j)
print(type(dj))
print(dj)
