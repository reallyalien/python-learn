# 要发送POST请求，只需要把get()方法变成post()，然后传入data参数作为POST请求的数据：

import requests

url = 'http://127.0.0.1:9087/ajax/testPost'
# requests默认使用application/x-www-form-urlencoded对POST数据编码
# requests.post(url, data={'form_email': 'abc@example.com', 'form_password': '123456'})

# 如果要传递JSON数据，可以直接传入json参数：# 内部自动序列化为JSON
r = requests.post(url, json={'name': 'a'}, timeout=2.5)

# 类似的，上传文件需要更复杂的编码格式，但是requests把它简化成files参数：

# upload_file = {'file', open('1.txt', 'rb')}
# requests.post(url, files=upload_file)

print(r.json())
print(r.headers)
print(r.cookies)
