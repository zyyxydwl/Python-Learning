#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/25 18:15
# @Author    : zhouyuyao
# @File      : four.py

# 习题
# 1. 输入三个整数x,y,z，请把这三个数由小到大输出。
# 1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
# 然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

# 一种
# sortNum=[]
# for i in range(3):
#     x=input("Please input a number : ")
#     sortNum.append(x)
# print(sorted(sortNum))
#
# # 两种
# list1=list()
# a=input("Please input a number : ")
# list1.append(a)
# b=input("Please input a number : ")
# list1.append(b)
# c=input("Please input a number : ")
# list1.append(c)
#
# print(list1.sort())

# 三种
# list1 = []
# x = input("please input the first number:")		#接收第一个数字
# list1.append(x)				#追加到列表
#
# y = input("please input the second number:")	#接收第二个数字
# list1.append(y)				#追加到列表
#
# z = input("please input the third number:")		#接收第三个数字
# list1.append(z)				#追加到列表
#
# list1.sort()				#利用列表的方法，对三个数进行排序
# print("{0} < {1} < {2}".format(list1[0], list1[1], list1[2]))	#输出



# 2. 企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，
# 高于10万元的部分，可可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，
# 高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

# x > y > z
# x > y < z
# x < y < z
# x < y > z 这几种情况。

x = input("please input the first number:")		#接收第一个数字
y = input("please input the second number:")	#接收第二个数字
z = input("please input the third number:")		#接收第三个数字

if x > y :                          #若x大于y则交换x,y的值
    x, y = y, x                     #交换x，y的值
    if x > z :
        x, z = z, x
                                    #在这个位置x为最小了，接下来比较y和z
        if y > z :
            y, z = z, y
                                    #在这个位置x < y < z
else:                               #x小于y，不用交换
    if x > z :                      #若x大于z则交换x，z的值
        x, z = z, x                 #交换x，z的值，
                                    #在这个位置x为最小了，接下来比较y和z
        if y > z :
            y, z = z, y
                                         # 在这个位置x < y < z
print("{0} < {1} < {2}".format(x,y,z))




