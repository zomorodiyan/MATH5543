import unittest
from fdm.fd5p import fd5p
import numpy as np


class TestHomework2(unittest.TestCase):
    def test_fd5p_existance(self):
        print(np.zeros(1))
        fd5p(3, 3)

    def test_fd5p_returns_two_matrixes(self):
        A, B = fd5p(3, 3)


if __name__ == "__main__":
    unittest.main()
