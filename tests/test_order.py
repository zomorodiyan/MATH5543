import unittest
from fdm.order import order


class TestOrder(unittest.TestCase):
    def test_input_data_type(self):
        with self.assertRaises(TypeError):
            order([[1, 2, 3], "A"])


if __name__ == "__main__":
    unittest.main()
