"""
1、字符串
字符串英文 string ，是 python 中随处可见的数据类型，字符串的识别也非常地简单，就是用「引号」括起来的。
引号包括单引号 ' ' ，双引号 " " 和 三引号 ''' ''' ，比如 'abc' ，"123" 等等。
这里请注意，单引号 '' 或双引号 "" 本身只是一种表示方式，不是字符串的一部分，因此，字符串 'abc' 只有 a，b，c 这 3 个字符。
如果善于思考的你，一定会问？
为什么要有单引号 ' ' ，双引号 " " 和 三引号 ''' ''' 啊，直接定死一个不就好了，搞那么麻烦，那么多规则表达同一个东西干嘛？
对，一般来说一种语法只用一个规则来表示是最好的，竟然现在字符串有三种不同的表示，证明是有原因的。
那么我们先来看下这三种方式，来定义同样内容的字符串，再把它打印出来，看看是怎样的。
"""
str1='fanyc'
str2="fanyc"
str3='''fanyc'''
print(str1)
print(str2)
print(str3)

#打印出来的结果是一样的。

# 但是要注意，用单引号 ' ' 不行，用双引号 " " 是可以的。

string1="fan'y'c"
print(string1)

string2='''f"a'n'y"c'''
print(string2)

# fanyc
# fanyc
# fanyc
# fan'y'c
# f"a'n'y"c
"""
那么用单引号，双引号定义的字符串就不能表示这样的内容吗？
并不是的，你可以使用转义字符。
比如单引号，你可以使用 \' 来表示，双引号可以使用 \" 来表示。
注意，这里的是反斜杠 \, 不是斜杆 / 。
了解了之后，直接程序测试一下：
"""
string1="fan\'y\'c"
print(string1)

string2='''f\"a\'n\'y\"c'''
print(string2)

# 三引号 ''' ''' 是直接可以分行的。

string='''fan
y
c'''
print(string)
