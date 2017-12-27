#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time      : 2017/12/26 20:50
# @Author    : zhouyuyao
# @File      : ninePaper.py


# 4.九宫格
# ABC     A:1-9; B:1-9 -A; C=1-9 -A-B
# EFG
# HIJ

class NinePaper(object):
    def __init__(self):
        print('''
             ______________
            |____|____|____|
            |____|____|____|
            |____|____|____|
            A,B,C,E,F,G,H,I,J必须是1-9，所有行和列的三个数相加都等于15
        ''')
        self.numbers=list()
        for i in range(1,10):
            self.numbers.append(i)
        print("number = {0}".format(self.numbers))

    def run(self):
        for A in range(1,10):
            l1=list()
            l1+=self.numbers
            l1.remove(A)
            for B in l1:
                l2=list()
                l2+=l1
                l2.remove(B)
                for C in l2:
                    l3=list()
                    l3+=l2
                    l3.remove(C)
                    for D in l3:
                        l4=list()
                        l4+=l3
                        l4.remove(D)
                        for E in l4:
                            l5=list()
                            l5+=l4
                            l5.remove(E)
                            for F in l5:
                                l6=list()
                                l6+=l5
                                l6.remove(F)
                                for G in l6:
                                    l7=list()
                                    l7+=l6
                                    l7.remove(G)
                                    for H in l7:
                                        l8=list()
                                        l8+=l7
                                        l8.remove(H)
                                        for I in l8:
                                                if A+B+C==E+F+D==H+I+G==A+E+I==B+E+H==C+G+E==A+E+I==C+F+I==15:
                                                    print('''        
 ___________
|_{0}_|_{1}_|_{2}_|
|_{3}_|_{4}_|_{5}_|
|_{6}_|_{7}_|_{8}_|
            '''.format(A,B,C,D,E,F,G,H,I))

        # ABC
        # DEF
        # GHI

def main():
    ninePaper=NinePaper()
    ninePaper.run()

if __name__ == '__main__':
    main()


