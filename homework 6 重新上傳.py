# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 16:23:48 2021

@author: USER
"""

score = []
for s in range(1,6,1):
    k = input()
    k = int(k)
    score.append(k)
print(*score)
sum = 0
for s in range(0,5,1):
    sum = sum + score[s]
print(sum/5)
m = 0
for k in range(0,5,1):
    if(m<score[k]):
        m = score[k]
print(m)
m = 1000
for s in range(0,5,1):
    if(m>score[s]):
        m = score[s]
print(m)
