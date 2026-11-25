from mininum import Array
from mininum.algorithms import (
    linear_search,
    binary_search,
    merge_sort,
    quick_sort,
    bubble_sort,
    quick_select,
    unique_set,
    top_k,
)


def test_linear_search():
    a = Array([10, 20, 30, 40, 50], (5,))
    b = Array([], (0,))
    c = Array([-5, -2, 0, 3], (4,))
    assert linear_search(a, 30) == 2
    assert linear_search(a, 10) == 0
    assert linear_search(a, 60) == -1
    assert linear_search(b, 10) == -1
    assert linear_search(c, -2) == 1


def test_binary_search():
    a = Array([10, 20, 30, 40, 50], (5,))
    b = Array([], (0,))
    c = Array([-5, -2, 0, 3], (4,))

    assert binary_search(a, 30) == 2
    assert binary_search(a, 10) == 0
    assert binary_search(a, 60) == -1
    assert binary_search(b, 10) == -1
    assert binary_search(c, -2) == 1


def test_bubble_sort():
    a = Array([5, 3, 8, 1, 2], (5,))
    b = Array([], (0,))
    c = Array([4, 3, 2, 1], (4,))
    d = Array([5, 5, 2, 2], (4,))

    assert (bubble_sort(a.copy()) == Array([1, 2, 3, 5, 8], (5,)))
    assert bubble_sort(b.copy()) == Array([], (0,))
    assert bubble_sort(c.copy()) == Array([1, 2, 3, 4], (4,))
    assert bubble_sort(d.copy()) == Array([2, 2, 5, 5], (4,))

def test_selection_sort():
    a = [5, 3, 8, 1, 2]
    b = []
    c = [4, 3, 2, 1]

    assert selection_sort(a.copy()) == [1, 2, 3, 5, 8]
    assert selection_sort(b.copy()) == []
    assert selection_sort(c.copy()) == [1, 2, 3, 4]


def test_merge_sort():
    a = [5, 3, 8, 1, 2]
    b = []
    c = [4, 3, 2, 1]
    d = [5, 5, 2, 2]

    assert merge_sort(a) == [1, 2, 3, 5, 8]
    assert merge_sort(b) == []
    assert merge_sort(c) == [1, 2, 3, 4]
    assert merge_sort(d) == [2, 2, 5, 5]


def test_quick_sort():
    a = [5, 3, 8, 1, 2]
    b = []
    c = [4, 3, 2, 1]
    d = [5, 5, 2, 2]

    assert quick_sort(a) == [1, 2, 3, 5, 8]
    assert quick_sort(b) == []
    assert quick_sort(c) == [1, 2, 3, 4]
    assert quick_sort(d) == [2, 2, 5, 5]


def test_quick_select():
    a = [12, 4, 7, 2, 15, 9, 1, 6]

    assert quick_select(a.copy(), 0) == 1
    assert quick_select(a.copy(), 1) == 2
    assert quick_select(a.copy(), 3) == 6
    assert quick_select(a.copy(), 7) == 15


def test_has_duplicates():
    a = [1, 2, 3, 4, 5]
    b = [1, 2, 3, 2, 5]
    c = []
    d = [7]

    assert has_duplicates(a) == False
    assert has_duplicates(b) == True
    assert has_duplicates(c) == False
    assert has_duplicates(d) == False
