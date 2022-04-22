import unittest
from fdm.fd5p import fdm2Dmatrix, fdm2Drhs
import matplotlib.pyplot as plt
import numpy as np


class TestHomework2(unittest.TestCase):
    def test_problem_1(self):
        err = np.zeros(3)
        nxz = np.array([10, 20, 40])
        dxz = np.array([1 / 10, 1 / 20, 1 / 40])
        dxz2 = np.array([1 / 100, 1 / 400, 1 / 1600])
        # for ik,(nx,ny) in enumerate([[10, 30],[20, 60],[40, 120],[80,240]]):
        # for ik,(nx,ny) in enumerate([[10, 30],[20, 60],[40, 120]]):
        for ik, (nx, ny) in enumerate([[10, 30]]):
            print("(nx, ny) =", (nx, ny))
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
            print("coefficient matrix")
            A = fdm2Dmatrix(nx=nx, ny=ny, dx=dx, dy=dy)
            assert type(A) is np.ndarray, "fdm2Dmatrix output is not np.ndarray"

            x = np.linspace(a, b, nx + 2)
            y = np.linspace(c, d, ny + 2)
            xv, yv = np.meshgrid(x, y)

            # right hand side
            print("right hand side")
            B = fdm2Drhs(funF=funF, funG=funG, xv=xv, yv=yv, nx=nx, dx=dx, ny=ny, dy=dy)
            assert type(B) is np.ndarray, "fdm2Drhs output is not np.ndarray"
            print("solving...")
            sol = np.linalg.solve(A, B)
            print("done!")

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
            if ik == 2:
                plt.figure()
                plt.plot(nxz, err)
                plt.plot(nxz, dxz)
                plt.plot(nxz, dxz2)
                plt.xscale("log")
                plt.yscale("log")
                plt.legend()
                plt.savefig("./Plots/err.png")

            print(" ---- plotting ...  ---- ")
            plt.figure()
            plt.contourf(xv, yv, field)
            plt.savefig("./Plots/1b_contour.png")
            print(" ---- plotting done ---- ")


if __name__ == "__main__":
    unittest.main()
