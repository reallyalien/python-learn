import requests

url = 'http://127.0.0.1:9087/ajax/testGet'
resp = requests.get(url)
print(resp.status_code)
print(resp.text)
# 实际请求的URL
print(resp.url)
# 自动检测编码
print(resp.encoding)
# 无论响应是文本还是二进制内容，我们都可以用content属性获得bytes对象：
print(resp.content)
# 对于带参数的URL，传入一个dict作为params参数：
#
# >>> r = requests.get('https://www.douban.com/search', params={'q': 'python', 'cat': '1001'})
# >>> r.url # 实际请求的URL
# 'https://www.douban.com/search?q=python&cat=1001'


# requests的方便之处还在于，对于特定类型的响应，例如JSON，可以直接获取：
print(resp.json())

# 需要传入HTTP Header时，我们传入一个dict作为headers参数：
r = requests.get('https://www.douban.com/',
                 headers={'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit'})
