import pickle

d = dict(name='bob', age=10)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件
print(pickle.dumps(d))
print('---------------------------------------------------')
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# f = open('/home/wangtao/baidu/1.txt', 'wb')
# pickle.dump(d, f)

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open('/home/wangtao/baidu/1.txt', 'rb')
pickle.load(f)
f.close()
print(d)
