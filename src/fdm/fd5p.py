# 2D mesh with Dirichlet Boundary condition 5-point stencil
# make matrix A and B for Ax=B system of equations
import numpy as np


def fd5p(m, n):
    # Eq.: ∇^2(u) = −(π^2 + 1).sin(πx).sin(y)
    """
    a = 0
    b = 1
    c = 0
    d = np.pi
    def funF(x,y)
        return -(np.pi**2 +1)*np.sin(np.pi*x)*np.sin(y)
    def funG(x,y)
        return 0
    """
    print(np.zeros(1))
    """
    domain = [a,b,c,d]
    m = 10;
    n = 30;
    hx = (b-a)/(m+1);
    hy = (d-c)/(n+1);


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

    BCL =2 # left boundary condition
    BCU =3 # up boundary condition
    BCR =4 # right boundary condition
    BCD =5 # bottom boundary condition
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
    """
    return 1, 2


fd5p(3, 3)
