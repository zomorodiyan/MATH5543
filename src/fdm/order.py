import numpy as np


def order(data):
    if (type(data[0]) not in [list, np.ndarray]) or (
        type(data[1]) not in [list, np.ndarray]
    ):
        raise TypeError("input data (x and y) must be and array of numbers")
