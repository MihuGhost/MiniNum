from mininum import Array
from mininum.exceptions import ShapeError

"""
PHASE 3
"""


def test_addition():
    a = Array([1, 2, 3, 4, 5, 6], (3, 2))
    b = Array([1, 2, 3, 4, 5, 6], (3, 2))

    assert (a + b).data == [2, 4, 6, 8, 10, 12]
    assert (a + b).shape == (3, 2)


def test_subtraction():
    a = Array([2, 4, 6, 8, 10, 12], (3, 2))
    b = Array([1, 2, 3, 4, 5, 6], (3, 2))

    assert (a - b).data == [1, 2, 3, 4, 5, 6]
    assert (a - b).shape == (3, 2)


def test_multiplication():
    a = Array([1, 2, 3, 4, 5, 6], (3, 2))
    assert (a * 2).data == [2, 4, 6, 8, 10, 12]
    assert (a * 2).shape == (3, 2)


def test_division():
    a = Array([2, 4, 6, 8, 10, 12], (3, 2))

    assert (a / 2).data == [1, 2, 3, 4, 5, 6]
    assert (a / 2).shape == (3, 2)


def test_reverse_subtraction():
    a = Array([1, 2, 3, 4, 5, 6], (3, 2))

    assert (10 - a).data == [9, 8, 7, 6, 5, 4]
    assert (10 - a).shape == (3, 2)


def test_comparison():
    a = Array([1, 2, 3, 4, 5, 6], (3, 2))
    b = Array([2, 1, 2, 6, 4, 7], (3, 2))

    assert (a < b).data == [True, False, False, True, False, True]
    assert (a < b).shape == (3, 2)


def test_not_equal():
    a = Array([1, 2, 3, 4, 5, 6], (3, 2))
    b = Array([2, 1, 2], (3,))

    assert (a == b) == False


def test_equal():
    a = Array([2, 1, 2, 6, 4, 7], (3, 2))
    b = Array([2, 1, 2, 6, 4, 7], (3, 2))

    assert (a == b) == True


def test_shape_match():
    a = Array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], (2, 2, 3))
    b = Array([1, 2, 3, 4, 5, 6], (2, 1, 3))
    c = Array([1, 2, 3, 4, 5, 6], (2, 3))
    d = Array([1, 2, 3, 4], (2, 2))

    assert (a + b).data == [2, 4, 6, 5, 7, 9, 11, 13, 15, 14, 16, 18]
    assert (a + b).shape == (2, 2, 3)
    assert (a < b).data == [False, False, False, False, False, False, False, False, False, False, False, False]
    assert (a < b).shape == (2, 2, 3)
    assert (a + c).data == [2, 4, 6, 8, 10, 12, 8, 10, 12, 14, 16, 18]
    assert (a + c).shape == (2, 2, 3)

    try:
        a + d
        assert False, "Expected ShapeError"
    except ShapeError:
        pass
