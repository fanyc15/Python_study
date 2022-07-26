import datetime
# 在 Python 提供了 for 循环和 while 循环。
#
# 这里又有一个问题了，如果我想让他运行了一百次之后停止，那该怎么做呢？
#
# 这时候需要用到一些控制循环的语句：
#
# 循环控制语句	描述
# break	在语句块执行过程中终止循环，并且跳出整个循环
# continue	在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环
# pass	pass 是空语句，是为了保持程序结构的完整性


print("________________________________________________")
dict1={'美团':"qqq",'百度':'456'}
for i in  dict1:
    print(i)
# 你会发现只打印了字典 dict 中的每一个 key 值。
# 3、 range() 函数
# for 循环还常常和 range() 函数搭配使用的。
#
# 如果不知道 range() 函数 , 我们直接通过一段程序来理解。
#
print("______________________")
for i in range(3):
    print(i)

print("_________________________")


sum=0
count=1
while count <=100:
    sum =sum+count
    count=count+1
print(sum)


# 5、for 循环和 whlie 循环的区别
# 之前也提到过了，如果一种语法能表示一个功能，那没必要弄两种语法来表示。
#
# 竟然都是循环，for 循环和 while 循环肯定有他们的区别的。
#
# 那什么时候才使用 for 循环和 while 循环呢？
#
# for 循环主要用在迭代可迭代对象的情况。
#
# while 循环主要用在需要满足一定条件为真，反复执行的情况。 （死循环+break 退出等情况。）
#
# 部分情况下，for 循环和 while 循环可以互换使用。

