'''
6、List（列表）运算符
列表对 + 和 * 的操作符与字符串相似。+ 号用于组合列表，* 号用于重复列表。

Python 表达式	                结果	                            描述
len([1, 2, 3])	                3	                            计算元素个数
[1, 2, 3] + [4, 5, 6]	        [1, 2, 3, 4, 5, 6]	            组合
['Hi!'] * 4	                    ['Hi!', 'Hi!', 'Hi!', 'Hi!']	复制
3 in [1, 2, 3]	                True	                        元素是否存在于列表中
for x in [1, 2, 3]: print x,	1 2 3	                        迭代
'''
'''
7、List （列表）函数&方法
函数&方法	                        描述
len(list)	                    列表元素个数
max(list)	                    返回列表元素最大值
min(list)	                    返回列表元素最小值
list(seq)	                    将元组转换为列表
list.append(obj)	            在列表末尾添加新的对象
list.count(obj)	                统计某个元素在列表中出现的次数
list.extend(seq)	            在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
list.index(obj)	                从列表中找出某个值第一个匹配项的索引位置
list.insert(index, obj)	        将对象插入列表
list.pop(obj=list[-1])	        移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
list.remove(obj)	            移除列表中的一个元素（参数是列表中元素），并且不返回任何值
list.reverse()	                反向列表中元素
list.sort([func])	            对原列表进行排序
'''
list=[111,222,333,444]
list1=["张1","张12","张3","zhansan"]
seq={555,666}
list2=[777,888]
print(len(list))
print(max(list1))       # 张3
print(min(list1))       # zhansan
print(list.append("zh张6"))
print(list)
print(list1.count('zhansan'))
print(list.extend(seq))             #  注意是队列
print(list)
print(list.index('zh张6'))
print(list.insert(8, '123'))
print(list)
# list.pop(object=list[-1])
print(list.remove('123'))              #  注意引号 因为是集合是需要完整匹配的
# del list[-1]
print(list)
print(list.reverse())
print(list)


# 排序
# list.sort(cmp=None, key=None, reverse=False)
# cmp -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。
# key -- 主要是用来进行比较的元素，只有一个参数，具体的函数的参数就是取自于可迭代对象中，指定可迭代对象中的一个元素来进行排序。
# reverse -- 排序规则，reverse = True 降序， reverse = False 升序（默认）。
aList = ['123', 'Google', 'Runoob', 'Taobao', 'Facebook'];

print(aList.sort())
print("List : ")
print(aList)
# 列表
vowels = ['e', 'a', 'u', 'o', 'i']

# 降序
vowels.sort(reverse=True)

# 输出结果
print('降序输出:')
print(vowels)


# 获取列表的第二个元素
def takeSecond(elem):
    return elem[1]


# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]

# 指定第二个元素排序
random.sort(key=takeSecond)

# 输出类别
print('排序列表：')
print(random)