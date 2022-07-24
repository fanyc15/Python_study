# 1、函数的参数类型
# 设置与传递参数是函数的重点，而 Python 的函数对参数的支持非常的灵活。
#
# 主要的参数类型有：默认参数、关键字参数（位置参数）、不定长参数。
#
# 下面我们将一一了解这几种参数。

# 2、默认参数
# 有时候，我们自定义的函数中，如果调用的时候没有设置参数，需要给个默认值，这时候就需要用到默认值参数了。
#
# 默认参数，只要在构造函数参数的时候，给参数赋值就可以了
#
# 例如：

def print_user_info(name='无名', age='未知', sex='未知'):
    # 打印用户信息
    print('昵称：{}'.format(name), end='    ')
    print('年龄：{}'.format(age), end='     ')
    print('性别：{}'.format(sex))
    return;


# 调用 print_user_info 函数

print_user_info('两点水', 18, '女')
print_user_info('三点水', 25, '男')
print_user_info()

print('_________________________________')


# 从输出结果可以看到，当你设置了默认参数的时候，在调用函数的时候，不传该参数，就会使用默认值。
#
# 但是这里需要注意的一点是：只有在形参表末尾的那些参数可以有默认参数值，也就是说你不能在声明函数形参的时候，先声明有默认值的形参而后声明没有默认值的形参。
#
# 这是因为赋给形参的值是根据位置而赋值的。例如，def func(a, b=1) 是有效的，但是 def func(a=1, b) 是 无效 的。
#
# 默认值参数就这样结束了吗？
#
# 还没有的，细想一下，如果参数中是一个可修改的容器比如一个 lsit （列表）或者 dict （字典），那么我们使用什么来作为默认值呢？

# 我们可以使用 None 作为默认值。就像下面这个例子一样：

# 如果 b 是一个 list ，可以使用 None 作为默认值
def print_info(a, b=None):
    if b is None:
        b = []
    return;


print((print_info(1)))
print('_________________________________')


def print_info(a, b=[]):
    return;


print((print_info(1)))

print('_________________________________')


def print_info(a, b=[]):
    print(b)
    return b;


result = print_info(1)

result.append('error')

print_info(2)

print('_________________________________')
_no_value = object()


def print_info(a, b=_no_value):
    if b is _no_value:
        print('b 没有赋值')
    return;


# 这里的 object 是 python 中所有类的基类。 你可以创建 object 类的实例，但是这些实例没什么实际用处，因为它并没有任何有用的方法，
# 也没有任何实例数据(因为它没有任何的实例字典，你甚至都不能设置任何属性值)。 你唯一能做的就是测试同一性。也正好利用这个特性，来判断是否有值输入。

# 一般情况下，我们需要给函数传参的时候，是要按顺序来的，如果不对应顺序，就会传错值。
#
# 不过在 Python 中，可以通过参数名来给函数传递参数，而不用关心参数列表定义时的顺序，这被称之为关键字参数。
#
# 使用关键参数有两个优势 ：
#
# 由于我们不必担心参数的顺序，使用函数变得更加简单了。
#
# 假设其他参数都有默认值，我们可以只给我们想要的那些参数赋值

# 3、关键字参数（位置参数）
def print_user_info(name, age, sex='男'):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex))
    return;


# 调用 print_user_info 函数

print_user_info(name='两点水', age=18, sex='女')
print_user_info(name='两点水', sex='女', age=18)


# 4、不定长参数
# 或许有些时候，我们在设计函数的时候，我们有时候无法确定传入的参数个数。
#
# 那么我们就可以使用不定长参数。
#
# Python 提供了一种元组的方式来接受没有直接定义的参数。这种方式在参数前边加星号 * 。
#
# 如果在函数调用时没有指定参数，它就是一个空元组。我们也可以不向函数传递未命名的变量。
#
# 例如：

def print_user_info(name, age, sex='男', *hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex), end=' ')
    print('爱好：{}'.format(hobby))
    return;


# 调用 print_user_info 函数
print_user_info('两点水', 18, '女', '打篮球', '打羽毛球', '跑步')
# 通过对比上面的例子和这个例子，可以知道，*hobby是可变参数，且 hobby其实就是一个 tuple （元祖），**hobby是关键字参数，且 hobby 就是一个 dict （字典）
print('_________________________________')


def print_user_info(name, age, sex='男', **hobby):
    # 打印用户信息
    print('昵称：{}'.format(name), end=' ')
    print('年龄：{}'.format(age), end=' ')
    print('性别：{}'.format(sex), end=' ')
    print('爱好：{}'.format(hobby))
    return;


# 调用 print_user_info 函数
print_user_info(name='两点水', age=18, sex='女', hobby=('打篮球', '打羽毛球', '跑步'))
# 5、只接受关键字参数
#
# 关键字参数使用起来简单，不容易参数出错，那么有些时候，我们定义的函数希望某些参数强制使用关键字参数传递，这时候该怎么办呢？
#
# 将强制关键字参数放到某个*参数或者单个*后面就能达到这种效果,比如：

print("_______________________________")


def recv(maxsize, *, block):
    """接收一条消息"""
    pass


recv(1024, True)  # 错误写法会产生TypeError错误
# TypeError: recv() takes 1 positional argument but 2 were given

recv(1024, block=True)  # 正确
print("_______________________________________")


# 使用这种方法，我们还能在接受任意多个位置参数的函数中指定关键字参数。比如：


def mininum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


ret1 = mininum(1, 5, 2, -5, 10)
print(ret1)  # ret1 = -5
ret2 = mininum(1, 5, 2, -5, 10, clip=0)
print(ret2)  # ret2 = 0

# 在很多情况下，使用强制关键字参数会比使用位置参数表意更加清晰，程序也更加具有可读性。例如，考虑一下下面这个函数调用：

# msg = recv(1024, False)
# 如果调用者对recv函数不是很熟悉，那么调用者就会不明白那个False参数是用来干嘛的。
#
# 但是，如果代码变成下面这样，就清楚很多了。
# msg = recv(1024, block=False)
