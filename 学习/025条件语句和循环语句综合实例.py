# 打印九九乘法表
for i in range(1, 10):
        for j in range(1, i+1):
            # 打印语句中，大括号及其里面的字符 (称作格式化字段) 将会被 .format() 中的参数替换,注意有个点的
            print('{}x{}={}\t'.format(i, j, i*j),end="")
            # print('%d*%d=%d\t' % (x, y, x * y), end='')

        print()
print("________________________________")

x=y=1
while y<=9:  #y为行数
    x=1 #每一行都得从1开始
    while x<=y:
        print('%d*%d=%d\t'%(x,y,x*y),end='')  #end为空是为了不让他换行
        x+=1
    print()
    y+=1

print("________________________________")
# 2、判断是否是闰年

year = int(input("请输入一个年份: "))
if (year % 4) == 0 and (year % 100) != 0 or (year % 400) == 0:
    print('{0} 是闰年' .format(year))
else:
     print('{0} 不是闰年' .format(year))

