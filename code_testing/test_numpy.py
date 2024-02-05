import numpy as np


def test_matmul():
    x = np.random.randn(5, 10)
    y = np.random.randn(10)
    xy = np.matmul(x, y)
    assert xy.shape == (5,)
