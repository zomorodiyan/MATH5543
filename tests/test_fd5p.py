import unittest
from fdm.fd5p import fdm2Dmatrix, fdm2Drhs
from fdm.fd5p import trapezoidal
import matplotlib.pyplot as plt
import numpy as np


class TestHomework2(unittest.TestCase):
    def test_problem_1(self):
        # problem_1 was tested after coding (not TDD)
        err = np.zeros(3)
        nxz = np.array([10.0, 20.0, 40.0])
        dxz = nxz ** -1
        dxz2 = dxz ** 2
        for ik, (nx, ny) in enumerate([[10, 30], [20, 60], [40, 120]]):
            # Equation: ∇^2(u) = −(π^2 + 1).sin(πx).sin(y)
            def funF(x, y):
                return -(np.pi ** 2 + 1) * np.sin(np.pi * x) * np.sin(y)

            funG = 0
            domain = [0, 1, 0, np.pi]
            a = domain[0]
            b = domain[1]
            c = domain[2]
            d = domain[3]
            dx = (b - a) / (nx + 1)
            dy = (d - c) / (ny + 1)

            # coefficient matrix
            A = fdm2Dmatrix(nx=nx, ny=ny, dx=dx, dy=dy)
            assert type(A) is np.ndarray, "fdm2Dmatrix output is not np.ndarray"

            x = np.linspace(a, b, nx + 2)
            y = np.linspace(c, d, ny + 2)
            xv, yv = np.meshgrid(x, y)

            # right hand side
            B = fdm2Drhs(funF=funF, funG=funG, xv=xv, yv=yv, nx=nx, dx=dx, ny=ny, dy=dy)
            assert type(B) is np.ndarray, "fdm2Drhs output is not np.ndarray"
            sol = np.linalg.solve(A, B)

            # populate 2D field
            field = np.zeros_like(xv)  # b.c. already satisfied (=0)
            for k in range(len(sol)):
                i = k % nx + 1
                j = int(k / nx) + 1
                field[j, i] = sol[k]
                exact = np.sin(np.pi * i * dx) * np.sin(j * dy)
                error = abs(sol[k] - exact)
                if error > err[ik]:
                    err[ik] = error
            print("err", err)

            # problem 1-b
            if ik == 0:
                plt.figure()
                plt.contourf(xv, yv, field)
                # plt.savefig("./Plots/1b_contour.png")
                # plt.show()

            # problem 1-c
            if ik == 2:
                plt.figure()
                plt.plot(nxz, err)
                plt.plot(nxz, dxz)
                plt.plot(nxz, dxz2)
                plt.xscale("log")
                plt.yscale("log")
                plt.legend(["error", "h", "h^2"])
                # plt.savefig("./Plots/1c_error.png")
                # plt.show()

    def test_problem_2(self):
        # problem_2 was tested after coding (not TDD)
        a = 0
        b = 15
        U0 = 1
        N = 100
        Dfun = fun = 1

        def Dfun(u):
            return u ** 2 + 1

        def fun(u):
            return 2 * u

        U, t = trapezoidal(fun, Dfun, a, b, U0, N)
        assert type(U) is np.ndarray, 'fdm2Dmatrix output, "U" is not np.ndarray'
        assert type(t) is np.ndarray, 'fdm2Dmatrix output, "t" is not np.ndarray'


if __name__ == "__main__":
    unittest.main()
