'''
Python 中基本数据类型转换的方法有下面几个。

方法	说明
int(x [,base ])	        将x转换为一个整数
float(x )	            将x转换到一个浮点数
complex(real [,imag ])	创建一个复数
str(x )	                将对象 x 转换为字符串
repr(x )	            将对象 x 转换为表达式字符串
eval(str )	            用来计算在字符串中的有效 Python 表达式,并返回一个对象
tuple(s )	            将序列 s 转换为一个元组
list(s )	            将序列 s 转换为一个列表
chr(x )	                将一个整数转换为一个字符
unichr(x )	            将一个整数转换为 Unicode 字符
ord(x )	                将一个字符转换为它的整数值
hex(x )	                将一个整数转换为一个十六进制字符串
oct(x )	                将一个整数转换为一个八进制字符串
注：在 Python 3 里，只有一种整数类型 int，表示为长整型，没有 python2 中的 Long。

这里我们可以尝试一下这些函数方法。
'''

# 比如 int() 函数，将符合规则的字符串类型转化为整数 。
str1='100'
str2='151'
print(str1+str2)
print(int(str1)+int(str2))
# 注意这里是符合规则的字符串类型，如果是文字形式等字符串是不可以被 int() 函数强制转换的。
#
# 还有小数形式的字符串也是不能用 int() 函数转换的。

print(int(88.88))

