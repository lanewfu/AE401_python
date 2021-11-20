# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:52:40 2021

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
s = [1,2,3,4,5]
m = 0
for k in range(0,5,1):
    if(m<s[k]):
        m = s[k]
print(m)
s = [1,2,3,4,5]
m = 6
for k in range(0,5,1):
    if(m>s[k]):
        m = s[k]
print(m)