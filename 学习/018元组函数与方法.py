# 6、tuple （元组）运算符
# 与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
#
# Python 表达式	结果	描述
# len((1, 2, 3))	3	计算元素个数
# (1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	连接
# ('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	复制
# 3 in (1, 2, 3)	True	元素是否存在
# for x in (1, 2, 3): print(x)	1 2 3	迭代
print(len((1, 2, 3)))
print(len((1,2,3)+(4,5,6)))
print(('Hi!',) * 4)
print(3 in (1, 2, 3))
for x in (1, 2, 3): print(x)

# len(tuple)	计算元组元素个数
# max(tuple)	返回元组中元素最大值
# min(tuple)	返回元组中元素最小值
# tuple(seq)	将列表转换为元组