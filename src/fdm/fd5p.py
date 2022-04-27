# 2D mesh with Dirichlet Boundary condition 5-point stencil
# make matrix A and B for Ax=B system of equations
import numpy as np


def trapezoidal(fun, Dfun, a, b, U0, N):
    x = np.linspace(a, b, N)
    dx = abs(a - b) / (N - 1)
    y = np.full_like(x, U0)
    for i in range(N - 1):
        y[i + 1] = y[i] + dx / 2 * (fun(y[i]) + fun(y[i] + dx * fun(y[i])))
    return x, y


def fdm2Drhs(funF, funG, xv, yv, nx, dx, ny, dy):
    xc = 1 / (dy) ** 2
    yc = 1 / (dx) ** 2

    BCL = funG  # (L)eft boundary condition
    BCU = funG  # (U)p boundary condition
    BCR = funG  # (R)ight boundary condition
    BCD = funG  # (D)own boundary condition

    b = np.zeros(nx * ny)
    for i in range(len(b)):
        x = dx * (i % nx + 1)
        y = dy * (int(i / nx) + 1)
        b[i] = funF(x, y)
        if i % nx == 0:
            b[i] += -xc * BCL
        elif i % nx == nx - 1:
            b[i] += -xc * BCR
        if i < nx:
            b[i] += -yc * BCD
        elif nx * (ny - 1) <= i and i < nx * ny:
            b[i] += -yc * BCU
    return b


def fdm2Dmatrix(nx, ny, dx, dy):
    print("here 1")
    xc = 1 / (dy) ** 2
    yc = 1 / (dx) ** 2
    dia = -2 * xc - 2 * yc

    print("here 2")
    print("size", nx * ny)
    a = np.zeros((nx * ny, nx * ny))
    for i in range(nx * ny):
        for j in range(nx * ny):
            if i == j:
                a[i, j] = dia
            elif abs(i - j) == 1:
                if not ((i % nx == 0 and j == i - 1) or (j % ny == 0 and i == j - 1)):
                    a[i, j] = xc
            elif abs(i - j) == nx:
                a[i, j] = yc
    print("here 3")
    return a
