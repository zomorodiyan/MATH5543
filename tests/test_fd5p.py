import unittest
from hw2.fd5p import fd5p
import numpy as np
import pytest


class TestCircleAre(unittest.TestCase):
    def test_fd5p_existance(self):
        print(np.zeros(1))
        fd5p()

    # @pytest.mark.skip(reason="how to skip test")
    @pytest.mark.xfail
    def test_values(self):
        with self.assertRaises(ValueError):
            print(np.zeros(1))


if __name__ == "__main__":
    unittest.main()
