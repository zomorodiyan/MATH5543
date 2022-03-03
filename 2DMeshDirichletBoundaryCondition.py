# -*- coding: utf-8 -*-
"""
Created on Thu Mar  3 09:07:26 2022

@author: Reggie
"""

#2D mesh with Dirichlet Boundary condition
#make matrix A and B for Ax=B system of equations

import numpy as np



m = 3
hy =1
hx =1




g = 1/(hy)**2
h = 1/(hx)**2
dia = -2*g-2*h
test = (1,1)


a = np.zeros((m**2,m**2))
for i in range(m**2):
    for j in range(m**2):
        if i%m == 0 and j == i-1:
            pass
        elif j%m == 0 and i == j-1:
            pass
        elif i == j:
            a[i,j] = dia
        elif abs(i - j) == 1:
            a[i,j] = g
        elif abs(i-j) == m:
            a[i,j] = h

def f(i):
    return(i*2)

BCL =2
BCU =3
BCR =4
BCD =5
b = np.zeros(m**2)
for i in range(m**2):
    b[i] = f(i)
    if i%m == 0:
        b[i] += -g*BCL 
    elif i%m == m-1:
        b[i] += -g*BCR
    if i < m**2 - 1 and i >= m**2 -m:
        b[i] += -h*BCU
    elif i<m:
        b[i] += -h*BCD

        
solution = np.linalg.solve(a,b)   





































