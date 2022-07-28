# 函数传值问题

def change_number(b):
    b = 1000


b = 1
change_number(b)
print(b)


# 想一下为什么打印的结果是 1 ，而不是 1000 ？
# 这里主要是函数参数的传递中，传递的是类型对象，之前也介绍了 Python 中基本的数据类型等。
# 而这些类型对象可以分为可更改类型和不可更改的类型

def change_number(b):
    print('函数中一开始 b 的值：{}'.format(b))
    b = 1000
    print('函数中 b 赋值后的值：{}'.format(b))


b = 1
change_number(b)
print('最后输出 b 的值：{}'.format(b))
#
# 因此，在一开始的例子中，b = 1,创建了一个整形对象 1 ，变量 b 指向了这个对象，然后通过函数 change_number 时，按传值的方式复制了变量 b ,
# 传递的只是 b 的值，并没有影响到 b 的本身。具体可以看下修改后的实例，通过打印的结果更好地理解.
