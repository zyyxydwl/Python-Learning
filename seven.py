#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/10 10:45
# @Author    : zhouyuyao
# @File      : seven.py

# 1. 设计一个程序，从终端接收10个数字，并使用自己编写的排序函数，对10个数字排序后输出

# 实现快排
def quicksort(nums):
    if len(nums) <= 1:
        return nums

    # 左子数组
    less = []
    # 右子数组
    greater = []
    # 基准数
    base = nums.pop()

    # 对原数组进行划分
    for x in nums:
        if x < base:
            less.append(x)
        else:
            greater.append(x)

    # 递归调用
    return quicksort(less) + [base] + quicksort(greater)

def main():
    nums = [6,1,2,7,9,3,4,5,10,8]
    print(quicksort(nums))

main()




# 2. 设计一个函数，接收一个英文单词，从文件中查询该单词的汉语意思并返回






