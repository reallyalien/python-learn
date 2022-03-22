user_name = 'Charlie'
user_age = 8
'''
同时输出多个变量和字符串，
默认 sep的值是 ，重新输入sep就可以自定义,
默认 end的值是\n，重新输入end就可以自定义,
默认 file的值是sys.stdout，重新输入就可以自定义,
默认 flush 的值是false，一般不需要改变，提高性能
'''
print("读者名", user_name, "年龄", user_age, sep=' ', end='\n', flush=True)
