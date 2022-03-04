# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 10:38:25 2022

@author: surajitsahu511
"""

n=int(input('Enter the numbers : '))

nos=[]
primeNos=[]

for i in range(1,n):
    no=int(input())
    nos.append(no)

print(nos)
    
for j in nos :
    if(j%2==0):
        primeNos.append(j)
print(primeNos)
