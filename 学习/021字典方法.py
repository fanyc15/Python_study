# # 7、dict （字典） 的函数和方法
# # 方法和函数	描述
# # len(dict)	计算字典元素个数
# # str(dict)	输出字典可打印的字符串表示
# # type(variable)	返回输入的变量类型，如果变量是字典就返回字典类型
# # dict.clear()	删除字典内所有元素
# # dict.copy()	返回一个字典的浅复制
# # dict.values()	以列表返回字典中的所有值
# # popitem()	随机返回并删除字典中的一对键和值
# # dict.items()	以列表返回可遍历的(键, 值) 元组数组
#
# dict1={
#        'liangdianshui':'111111' ,
#        123:'222222' ,
#        (123,'tom'):'333333',
#        'twowater':'444444'
# }
# print(dict1)
#
# print(len(dict1))
#
# print(type(dict1))
# dict1.clear()
#
# dict1 = {'Name': 'Zara', 'Age': 7};
#
# dict2 = dict1.copy()
# print("New Dictinary : %s" % str(dict2))
#
# dict2 = dict1.values()
# print(dict2)
#
# car = {
#   "brand": "Porsche",
#   "model": "911",
#   "year": 1963
# }
#
# car.popitem()
#
# print(car)
# # popitem() 方法删除最后插入字典中的项目。在 3.7 之前的版本中，popitem() 方法删除一个随机项。
# #
# # 删除的项目是 popitem() 方法的返回值，以元组的形式。请看下面的例子。

dict1={
       'liangdianshui':'111111' ,
       (123,'tom'):'333333',
}
print(dict1)
dict1.clear()
print(dict1)


