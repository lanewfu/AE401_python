# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 16:32:55 2021

@author: USER
"""

score=[['A',80],['B',90],['C',100]]
m = 0;
m_index = 0 
for k in range(0,3,1):
    if(m<score[k][1]):
        m_index = k
        m = score[k][1]
print(score[m_index][0],m)
m = 1000
for s in range(0,3,1):
    if(m>score[s][1]):
        m_index = s
        m = score[s][1]
print(score[m_index][0],m)