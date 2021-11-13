# -*- coding: utf-8 -*-
"""
Created on Sat Nov 13 16:54:08 2021

@author: USER
"""

import random
num = random.randint(1,20)
s = input()
k = 1;
while (k <= 5):
     s = input()
     s = int(s)
     if s>num:
        print('太大了')
     elif s<num:
        print('太小了')
     else:
        print('答對了')
        print(k)
     k = k+1