"""
1.1、块注释
“#”号后空一格，段落件用空行分开（同样需要“#”号）
# 块注释
# 块注释
#
# 块注释
# 块注释

1.2、行注释
至少使用两个空格和语句分开，注意不要使用无意义的注释

# 正确的写法
x = x + 1  # 边框加粗一个像素

# 不推荐的写法(无意义的注释)
x = x + 1 # x加1

1.3、建议
在代码的关键部分(或比较复杂的地方), 能写注释的要尽量写注释

比较重要的注释段, 使用多个等号隔开, 可以更加醒目, 突出重要性

app = create_app(name, options)


# =====================================
# 请勿在此处添加 get post等app路由行为 !!!
# =====================================


if __name__ == '__main__':
    app.run()
"""


# 文档注释不限于中英文, 但不要中英文混用
#
# 文档注释不是越长越好, 通常一两句话能把情况说清楚即可
#
# 模块、公有类、公有方法, 能写文档注释的, 应该尽量写文档注释
