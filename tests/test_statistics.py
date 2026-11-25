# todo Welford’s one-pass algorithm for variance

from mininum import Array
from mininum.statistics import sum, min, max, mean, variance, standard_deviation, argmin, argmax, count, unique, median


def test_sum():
    a = Array([1, 2, 3, 4, 5], (5,))
    b = Array([], (0,))
    assert sum(a) == 15
    assert sum(b) == 0


def test_min():
    a = Array([3, -2, 5, 1], (4,))
    b = Array([], (0,))
    assert min(a) == -2

    try:
        min(b)
        assert False, "empty array"
    except ValueError:
        pass


def test_max():
    a = Array([3, -2, 5, 1], (4,))
    b = Array([], (0,))
    assert max(a) == 5

    try:
        max(b)
        assert False, "empty array"
    except ValueError:
        pass


def test_mean():
    a = Array([2, 4, 6, 8], (4,))
    b = Array([1, 3, 5, 7, 9], (5,))
    assert mean(a) == 5
    assert mean(b) == 5


def test_median():
    a = Array([2, 4, 6, 8], (4,))
    b = Array([1, 3, 5, 7, 9], (5,))
    assert median(a) == 5
    assert median(b) == 5


def test_variance():
    a = Array([2, 4, 6, 8], (4,))

    assert variance(a) == 5


def test_standard_deviation():
    a = Array([2, 4, 6, 8], (4,))

    assert abs(standard_deviation(a) - 2.2360679775) < 1e-9


def test_argmin():
    a = Array([5, 2, 8, -1], (4,))

    assert argmin(a) == 3


def test_argmax():
    a = Array([5, 2, 8, -1], (4,))

    assert argmax(a) == 2


def test_count():
    a = Array([1, 2, 2, 3, 2, 4], (6,))
    b = Array([], (0,))

    assert count(a, 2) == 3
    assert count(a, 5) == 0
    assert count(b, 2) == 0


def test_unique():
    a = Array([1, 2, 2, 3, 1, 4], (6,))
    b = Array([], (0,))
    assert unique(a) == [1, 2, 3, 4]
    assert unique(b) == []
