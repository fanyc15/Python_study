# isinstance() 函数来判断一个对象是否是一个已知的类型，类似 type()。
# isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。
# 如果要判断两个类型是否相同推荐使用 isinstance()。


# 通过 return [表达式] 语句用于退出函数，选择性地向调用方返回一个表达式。
# 不带参数值的 return 语句返回 None。
def sum(num1, num2):
    # 两数之和
    if not (isinstance(num1, (int, float)) and isinstance(num2, (int, float))):
        raise TypeError('参数类型错误')
    return num1 + num2


print(sum(1, 2))
# 还通过内置函数isinstance()进行数据类型检查，检查调用函数时参数是否是整形和浮点型。如果参数类型不对，会报错，提示 参数类型错误
# print(sum("11", 2))