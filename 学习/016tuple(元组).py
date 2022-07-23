# 二、tuple（元组）
# 1、什么是元组 （tuple）
# 上一节刚说了一个有序列表 List ，现在说另一种有序列表叫元组：tuple 。
#
# tuple 和 List 非常类似，但是 tuple 一旦初始化就不能修改。 也就是说元组（tuple）是不可变的，那么不可变是指什么意思呢？
#
# 元组（tuple） 不可变是指当你创建了 tuple 时候，它就不能改变了，也就是说它也没有 append()，insert() 这样的方法，但它也有获取某个索引值的方法，但是不能赋值。
#
# 那么为什么要有 tuple 呢？
#
# 那是因为 tuple 是不可变的，所以代码更安全。
#
# 所以建议能用 tuple 代替 list 就尽量用 tuple 。


# 2、怎样创建元组（tuple）

# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
#
# tuple1=('两点水','twowter','liangdianshui',123,456)
# tuple2='两点水','twowter','liangdianshui',123,456
# 创建空元组
#
# tuple3=()
# 元组中只包含一个元素时，需要在元素后面添加逗号
#
# tuple4=(123,)
# 如果不加逗号，创建出来的就不是 元组（tuple），而是指 123 这个数了。
#
# 这是因为括号 () 既可以表示元组（tuple），又可以表示数学公式中的小括号，这就产生了歧义。
#
# 所以如果只有一个元素时，你不加逗号，计算机就根本没法识别你是要进行整数或者小数运算还是表示元组。
#
# 因此，Python 规定，这种情况下，按小括号进行计算，计算结果自然是 123 ，而如果你要表示元组的时候，就需要加个逗号。
#
# 具体看下图 tuple4 和 tuple5 的输出值
tuple1=('两点水','twowter','liangdianshui',123,456)
tuple2='两点水','twowter','liangdianshui',123,456
tuple3=()
tuple4=(123,)
tuple5=(123)


print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)