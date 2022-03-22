add = "http://c.biancheng.net/python/,http://c.biancheng.net/shell/"
for i in add:
    if i == ',':
        # 终止循环
        break
    print(i, end="")
else:
    print("执行 else 语句中的代码")
print("\n执行循环体外的代码")
# 循环当中的else语句准确来说是包含在循环里面的，当遇到break语句时，就不会执行else语句的代码
