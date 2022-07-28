# -*- coding: UTF-8 -*-
"""
PyCharm 031匿名函数
2022年月28日
by Fanyc15
"""
# 有没有想过定义一个很短地回调函数，但又不想用 def 的形式去写一个那么长的函数，那么有没有快捷方式呢？
#
# 答案是有的。
#
# python 使用 lambda 来创建匿名函数，也就是不再使用 def 语句这样标准的形式定义一个函数。
#
# 匿名函数主要有以下特点：
#
# lambda 只是一个表达式，函数体比 def 简单很多。
# lambda 的主体是一个表达式，而不是一个代码块。仅仅能在 lambda 表达式中封装有限的逻辑进去。
# lambda 函数拥有自己的命名空间，且不能访问自有参数列表之外或全局命名空间里的参数。
# 基本语法
# lambda [arg1 [,arg2,.....argn]]:expression


sum = lambda num1, num2: num1 + num2;
print(sum(1, 2))

# 输出的结果是 3

num2 = 100
sum1 = lambda num1: num1 + num2;

num2 = 10000
sum2 = lambda num1: num1 + num2;

print(sum1(1))
print(sum2(1))

# 输出的结果是 两个10001
# 这主要在于 lambda 表达式中的 num2 是一个自由变量，在运行时绑定值，
# 而不是定义时就绑定，这跟函数的默认值参数定义是不同的。所以建议还是遇到这种情况还是使用第一种解法.
