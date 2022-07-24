def func(a, b, c, *args, **kwargs):
    print(a, end="   ")
    print(b, end="   ")
    print(c, end="   ")
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))
    print()
    pass


func(1, 2, 3, 12314, 1231312, 123312, 1231312312, student="学生", teacher="老师")
# 总结:
# args可以实现传入多个,但不确定几个的形参形式.实参传入python将其组织为元组（tuple）
# **kwarges 可以实现传入多个但不确定几个的键值对定义，实参传入后python将其组织为字典（dict）
