#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/28 20:22
# @Author    : zhouyuyao
# @File      : six.py

# 习题
# 1. 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
# 程序分析：对n进行分解质因数,应先找到一个最小的质数i,然后按下述步骤完成：
# (1)如果分解后商为1,则说明分解质因数的过程已经结束,打印出即可。
# (2)如果商不为1,则应打印出i的值,并用n除以i的商,作为新的正整数进行分解,
# 　重复执行第一步。
# (3)如果n不能被i整除,则i的值加1,重复执行第一步。

def reduceNum(n):          #定义一个分解质因数的函数
    '''题目：将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5'''
    print('{} = '.format(n),end='')
    if not isinstance(n, int) or n <= 0 :    # 第一种情况判断两个类型是否相同推荐使用isinstance()
        print('Please input a valid number !')
        exit(0)
    elif n in [1] :                          #第二种情况为1
        print('{}'.format(n))
    while n not in [1] : # 循环保证递归        #当n的值不在列表1中，进入while循环
        for index in range(2, int(n + 1)):   #定义分解的质数的范围是2到n
            if n % index == 0:               #如果质因数与质数的余数为0，取模 - 返回除法的余数
                n /= index                   #n=n/index的商，let n equal to it n/index
                if n == 1:                   # This is the point
                    print(index)             # The last one
                else :                       # index 一定是素数
                    print('{} *'.format(index),end='')
                break
reduceNum(1250895)
reduceNum(90)
reduceNum(23)



# while True:
#     number=input("Please input a number : ")
#     if number !='quit':
#         number = int(number)
#         if number<2:
#             print("Please input a number greater than 2.")
#             continue
#         list1=[1,]
#         while number !=1:
#             for i in range(2,int(number+1)):
#                 if number %i==0:
#                     number/=i
#                     list1.append(i)
#                     break
#         print(" * ".join(map(str,list1)))
#     else:
#         print("goodbye!")
#         break


# 给你一个其中包含不同的英文字母和标点符号的文本，你要找到其中出现最多的字母，返回的字母必须是小写形式，
# 当检查最想要的字母时，不区分大小写，所以在你的搜索中 "A" == "a"。 请确保你不计算标点符号，数字和空格，只计算字母。
# 如果你找到 两个或两个以上的具有相同的频率的字母， 返回那个先出现在字母表中的字母。
# 例如 -- “one”包含“o”，“n”，“e”每个字母一次，因此我们选择“e”。
# 输入: 用于分析的文本.
# 输出: 最常见的字母的小写形式。
# 前提::
# 密码只包含ASCII码符号
# 0 < len(text) ≤ 10的5次方
#
# def checkio(text):
#     #replace this for solution
#     return 'a'
#
# if __name__ == '__main__':
#     #These "asserts" using only for self-checking and not necessary for auto-testing
#     assert checkio("Hello World!") == "l", "Hello test"
#     assert checkio("How do you do?") == "o", "O is most wanted"
#     assert checkio("One") == "e", "All letter only once."
#     assert checkio("Oops!") == "o", "Don't forget about lower case."
#     assert checkio("AAaooo!!!!") == "a", "Only letters."
#     assert checkio("abe") == "a", "The First."
#     print("Start the long test")
#     assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
#     print("The local tests are done.")
#






