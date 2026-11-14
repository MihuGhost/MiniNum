from mininum import Array
from mininum.exceptions import ShapeError

"""
PHASE 3
"""


def test_addition():
    a = Array([1, 2, 3], (3,))
    b = Array([4, 5, 6], (3,))

    assert (a + b).data == [5, 7, 9]


def test_subtraction():
    a = Array([5, 6, 7], (3,))
    b = Array([1, 2, 3], (3,))

    assert (a - b).data == [4, 4, 4]


def test_multiplication():
    a = Array([1, 2, 3], (3,))

    assert (a * 2).data == [2, 4, 6]


def test_division():
    a = Array([10, 20, 30], (3,))

    assert (a / 10).data == [1, 2, 3]


def test_reverse_subtraction():
    a = Array([1, 2, 3], (3,))

    assert (10 - a).data == [9, 8, 7]


def test_comparison():
    a = Array([1, 5, 3], (3,))
    b = Array([2, 5, 1], (3,))

    assert (a < b).data == [True, False, False]


def test_shape_mismatch():
    a = Array([1, 2], (2,))
    b = Array([1, 2, 3], (3,))

    try:
        a + b
        assert False, "Expected ShapeError"
    except ShapeError:
        pass


def test_shape_match():
    arr = Array(
        [10, 20, 30, 11, 21, 31, 40, 50, 60, 41, 51, 61,
         101, 201, 301, 111, 211, 311, 401, 501, 601, 411, 511, 611],
        (2, 3, 2, 2)
    )

    a = Array([1, 2, 3, 4, 5, 6], (2, 3))
    b = Array([10, 20, 30], (3,))

    assert (a + b).data == [11, 22, 33, 14, 25, 36]
