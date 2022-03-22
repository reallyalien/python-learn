from urllib import request, parse

url = 'http://127.0.0.1:9087/ajax/testPost'

user = dict(name='a')
data = parse.urlencode([
    ('name', 'a')
])
# 只需要把参数data以bytes形式传入。

try:
    response = request.urlopen(url, data=data.encode('utf-8'))
    print(response)
except Exception as e:
    print(e)
