# 4、修改元组 （tuple）
# 可能看到这个小标题有人会疑问，上面不是花了一大段来说 tuple 是不可变的吗？
#
# 这里怎么又来修改 tuple （元组） 了。
#
# 那是因为元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，还有通过修改其他列表的值从而影响 tuple 的值。
#
# 具体看下面的这个例子：
#
#-*-coding:utf-8-*-
list1=[123,456]
tuple1=('两点水','twowater','liangdianshui',list1)
print(tuple1)
list1[0]=789
list1[1]=100
print(tuple1)
# 输出的结果：
#
# ('两点水', 'twowater', 'liangdianshui', [123, 456])
# ('两点水', 'twowater', 'liangdianshui', [789, 100])
# 可以看到，两次输出的 tuple 值是变了的。我们看看 tuple1 的存储是怎样的。
#
# 可以看到，tuple1 有四个元素，最后一个元素是一个 List ，List 列表里有两个元素。
#
# 当我们把 List 列表中的两个元素 124 和 456 修改为 789 和 100 的时候，从输出来的 tuple1 的值来看，好像确实是改变了。
#
# 但其实变的不是 tuple 的元素，而是 list 的元素。
#
# tuple 一开始指向的 list 并没有改成别的 list，所以，tuple 所谓的“不变”是说，tuple 的每个元素，指向永远不变。注意是 tupe1 中的第四个元素还是指向原来的 list ，是没有变的，我们修改的只是列表 List 里面的元素。

# 5、删除 tuple （元组）
# tuple 元组中的元素值是不允许删除的，但我们可以使用 del 语句来删除整个元组
#
# #-*-coding:utf-8-*-
#
tuple1=('两点水','twowter','liangdianshui',[123,456])
print(tuple1)
del tuple1
