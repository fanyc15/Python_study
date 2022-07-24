"""
2、整数
整数英文为 integer 。代码中的整数跟我们平常认识的整数一样，包括正整数、负整数和零，是没有小数点的数字。

Python 可以处理任意大小的整数，例如：1，100，-8080，0，等等。
"""
int1=1+2
int2=1-2
int3=1*2
int4=1/2

print(int1)
print(int2)
print(int3)
print(int4)

print(type(int1))
print(type(int2))
print(type(int3))
print(type(int4))


'''
可以看到 int4 是 float 类型，而 int1 ,int2,int3 都是 int 整数类型。
那么 float 是什么类型呢？
float 是浮点数类型，是我们下面会说到的。
'''