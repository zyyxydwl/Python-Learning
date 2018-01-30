#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2018/1/1 18:08
# @Author    : zhouyuyao
# @File      : fileReadWrite.py

# 习题
# 1. 现有一个文件test.txt ，内容如下：
# 1234efgh
# abcd5678
# with open("test.txt",'w') as fd:
#     fd.write("1234efgh\n")
#     fd.write("abcd5678")

# 要求读出文件内容，对内容的顺序进行编辑，然后重新写入到文件，使其为如下形式
# 12345678
# abcdefgh


# # open file
# fin = open("test.txt", "r")
# fout = open("out.txt", "w")
#
# # header line
# header = fin.readline()
# fout.write(header)
#
# # data lines
# for line in fin:
#     dat_in = line.split()
#     dat_in[3] = "5.2"                           # modify data
#     dat_out = " ".join(dat_in)
#     fout.write(dat_out+"\n")
#
# # close file
# fin.close()
# fout.close()




# 注意事项：使用pycharm的同学在调试程序时，如果程序对文件进行了操作，
# 然后手动修改了文件，则要在pycharm中，程序所在的目录上点击右键，
# 选择clean python compiled files，否则可能会报错



# 2. 将上周五生成的dict3，排序后写入到文件dict.txt中，要求格式为
# A 65
# B 66
# C 67
# ...
# x 120
# y 121
# z 122

dict3={'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73,
       'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82,
       'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, 'a': 97,
       'c': 99, 'b': 98, 'e': 101, 'd': 100, 'g': 103, 'f': 102, 'i': 105, 'h': 104,
       'k': 107, 'j': 106, 'm': 109, 'l': 108, 'o': 111, 'n': 110, 'q': 113, 'p': 112,
       's': 115, 'r': 114, 'u': 117, 't': 116, 'w': 119, 'v': 118, 'y': 121, 'x': 120, 'z': 122}

dict3.items()
print(dict3)


