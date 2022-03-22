# Get
# urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
from urllib import request


# ===================================================================================================
def parse(input):
    print('type:%s' % type(input))
    data = input.read()
    print('Status:', input.status, input.reason)
    for k, v in input.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', data.decode('utf-8'))


# ===================================================================================================
url = 'https://yiketianqi.com/api?unescape=1&version=v1&appid=85841439&appsecret=EKCDLT4I'
with request.urlopen(url) as f:
    pass
    # parse(f)

# 如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
req = request.Request('http://www.douban.com/')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    parse(f)
