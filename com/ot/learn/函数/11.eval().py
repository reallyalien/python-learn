# eval() 和 exec() 函数都属于 Python 的内置函数，由于这两个函数在功能和用法方面都有相似之处，所以将它们放到一节进行介绍。
# eval() 和 exec() 函数的功能是相似的，都可以执行一个字符串形式的 Python 代码（代码以字符串的形式提供），相当于一个 Python 的解释器。
# 二者不同之处在于，eval() 执行完要返回结果，而 exec() 执行完不返回结果（文章后续会给出详细示例）。
'''
eval() 函数的语法格式为：
eval(expression, globals=None, locals=None, /)


而 exec() 函数的语法格式如下：
exec(expression, globals=None, locals=None, /)


可以看到，二者的语法格式除了函数名，其他都相同，其中各个参数的具体含义如下：
expression：这个参数是一个字符串，代表要执行的语句 。该语句受后面两个字典类型参数 globals 和 locals 的限制，只有在 globals 字典和 locals 字典作用域内的函数和变量才能被执行。
globals：这个参数管控的是一个全局的命名空间，即 expression 可以使用全局命名空间中的函数。如果只是提供了 globals 参数，而没有提供自定义的 __builtins__，则系统会将当前环境中的 __builtins__ 复制到自己提供的 globals 中，然后才会进行计算；如果连 globals 这个参数都没有被提供，则使用 Python 的全局命名空间。
locals：这个参数管控的是一个局部的命名空间，和 globals 类似，当它和 globals 中有重复或冲突时，以 locals 的为准。如果 locals 没有被提供，则默认为 globals。
注意，__builtins__ 是 Python 的内建模块，平时使用的 int、str、abs 都在这个模块中。通过 print(dic["__builtins__"]) 语句可以查看 __builtins__ 所对应的 value。

'''
dic = {}
dic['b'] = 3
print(dic.keys())
exec("a=4", dic)
print(dic.keys())

# 上面的代码是在作用域 dic 下执行了一句 a = 4 的代码。可以看出，exec() 之前 dic 中的 key 只有一个 b。执行完 exec() 之后，
# 系统在 dic 中生成了两个新的 key，分别是 a 和 __builtins__。
# 其中，a 为执行语句生成的变量，系统将其放到指定的作用域字典里；__builtins__ 是系统加入的内置 key。

a = 10
b = 20
c = 30
g = {'a': 6, 'b': 8}  # 定义一个字典
t = {'b': 100, 'c': 10}  # 定义一个字典

# gt当中有重复的元素b，以local当中的为准
print(eval('a+b+c', g, t))

print("eval and exec different==========================")

print(exec('1+1'))
print(eval('1+1'))

# 提示 eval() 中不识别等号语法。
# eval("a=2")

# 需要注意的是，在使用 eval() 或是 exec() 来处理请求代码时，函数 eval() 和 exec() 常常会被黑客利用，成为可以执行系统级命令的入口点，进而来攻击网站。
# 解决方法是：通过设置其命名空间里的可执行函数，来限制 eval() 和 exec() 的执行范围。
