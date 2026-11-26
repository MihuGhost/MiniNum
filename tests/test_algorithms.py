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
    argsort,
    sort,
    partition_list,
    top_k_list,
    partition,
)


def test_linear_search():
    a = [10, 20, 30, 40, 50]
    b = []
    c = [-5, -2, 0, 3]
    assert linear_search(a, 30) == 2
    assert linear_search(a, 10) == 0
    assert linear_search(a, 60) == -1
    assert linear_search(b, 10) == -1
    assert linear_search(c, -2) == 1


def test_binary_search():
    a = [10, 20, 30, 40, 50]
    b = []
    c = [-5, -2, 0, 3]

    assert binary_search(a, 30) == 2
    assert binary_search(a, 10) == 0
    assert binary_search(a, 60) == -1
    assert binary_search(b, 10) == -1
    assert binary_search(c, -2) == 1


def test_bubble_sort():
    a = [5, 3, 8, 1, 2]
    b = []
    c = [4, 3, 2, 1]
    d = [5, 5, 2, 2]

    assert bubble_sort(a.copy()) == [1, 2, 3, 5, 8]
    assert bubble_sort(b.copy()) == []
    assert bubble_sort(c.copy()) == [1, 2, 3, 4]
    assert bubble_sort(d.copy()) == [2, 2, 5, 5]


def test_merge_sort():
    a = [5, 3, 8, 1, 2]
    b = []
    c = [4, 3, 2, 1]
    d = [5, 5, 2, 2]

    assert merge_sort(a.copy()) == [1, 2, 3, 5, 8]
    assert merge_sort(b.copy()) == []
    assert merge_sort(c.copy()) == [1, 2, 3, 4]
    assert merge_sort(d.copy()) == [2, 2, 5, 5]


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

    # Ture for unique, false for not unique
    assert unique_set(a) == True
    assert unique_set(b) == False
    assert unique_set(c) == True
    assert unique_set(d) == True


def test_top_k_list():
    a = [7, 2, 9, 4, 1, 8]
    b = [7, 2, 9, 4, 1]
    c = [7, 2, 9, 9, 1, 8]

    assert quick_sort(top_k_list(a, 3)) == [7, 8, 9]
    assert quick_sort(top_k_list(b, 1)) == [9]
    assert quick_sort(top_k_list(b, 0)) == []
    assert quick_sort(top_k_list(b, 5)) == [1, 2, 4, 7, 9]
    assert quick_sort(top_k_list(c, 3)) == [8, 9, 9]

    try:
        top_k_list(b, -1)
        assert False, "Expected ValueError"
    except ValueError:
        assert True

    try:
        top_k_list(b, 6)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


def test_top_k():
    a = Array([7, 2, 9, 4, 1, 8], (2, 3))
    b = Array([7, 2, 9, 4, 1], (5, 1))
    c = Array([7, 2, 9, 9, 1, 8], (2, 3))
    assert quick_sort(top_k(a, 3)) == [7, 8, 9]
    assert quick_sort(top_k(b, 1)) == [9]
    assert quick_sort(top_k(b, 0)) == []
    assert quick_sort(top_k(b, 5)) == [1, 2, 4, 7, 9]
    assert quick_sort(top_k(c, 3)) == [8, 9, 9]

    try:
        top_k(b, -1)
        assert False, "Expected ValueError"
    except ValueError:
        assert True

    try:
        top_k(b, 6)
        assert False, "Expected ValueError"
    except ValueError:
        assert True


# def test_argsort_list():
#     a = [30, 10, 30, 20]
#
#     assert argsort(a) == [1, 3, 0, 2]

def test_argsort():
    # Basic sorting
    a = Array([30, 10, 30, 20], (4,))
    assert argsort(a).data == [1, 3, 0, 2]

    # Duplicate values
    a = Array([5, 2, 5, 2, 5], (5,))
    assert argsort(a).data == [1, 3, 0, 2, 4]

    # Single element
    a = Array([42], (1,))
    assert argsort(a).data == [0]

    # Negative values
    a = Array([-3, 5, -1, 2], (4,))
    assert argsort(a).data == [0, 2, 3, 1]

    # Empty array
    a = Array([], (0,))
    assert argsort(a).data == []

    # Check output type and shape
    a = Array([30, 10, 20], (3,))
    result = argsort(a)
    assert isinstance(result, Array)
    assert result.shape == (3,)

    # 2D array with duplicate values
    a = Array(
        [30, 10, 30, 20, 10, 40],
        (2, 3)
    )
    result = argsort(a)
    assert result.data == [1, 4, 3, 0, 2, 5]
    assert result.shape == (2, 3)
    assert isinstance(result, Array)

    # 3D array with duplicate values
    a = Array(
        [8, 3, 8, 1, 5, 3, 9, 1, 4, 7, 5, 2],
        (2, 2, 3)
    )

    result = argsort(a)

    assert result.data == [3, 7, 11, 1, 5, 8, 4, 10, 9, 0, 2, 6]
    assert result.shape == (2, 2, 3)
    assert isinstance(result, Array)


def test_sort():
    a = Array([5, 3, 8, 1, 2], (5,))
    b = Array([5, 3, 8, 1, 2, 1], (2, 3))
    assert sort(a) == Array([1, 2, 3, 5, 8], (5,))
    assert sort(b) == Array([1, 1, 2, 3, 5, 8], (2, 3))


def test_partition_list():
    # Test 1: Normal case
    arr = [30, 10, 50, 20, 40]

    left, pivot, right = partition_list(arr, 0)

    assert left == [10, 20]
    assert pivot == 30
    assert right == [50, 40]

    # Test 2: Pivot at the last index
    arr = [30, 10, 50, 20, 40]

    left, pivot, right = partition_list(arr, 4)

    assert left == [30, 10, 20]
    assert pivot == 40
    assert right == [50]

    # Test 3: Duplicate values
    arr = [30, 10, 30, 20, 40]

    left, pivot, right = partition_list(arr, 0)

    assert left == [10, 30, 20]
    assert pivot == 30
    assert right == [40]

    # Test 4: Negative values
    arr = [-5, -10, 0, 5, -3]

    left, pivot, right = partition_list(arr, 0)

    assert left == [-10]
    assert pivot == -5
    assert right == [0, 5, -3]

    # Test 5: Single element
    arr = [10]

    left, pivot, right = partition_list(arr, 0)

    assert left == []
    assert pivot == 10
    assert right == []

    # Test 6: Empty array
    arr = []

    try:
        partition_list(arr, 0)
        assert False, "Expected IndexError"
    except IndexError:
        pass


def test_partition():
    # 1D array
    a = Array([30, 10, 30, 20], (4,))
    left, pivot, right = partition(a, 0)

    assert left.data == [10, 30, 20]
    assert pivot == 30
    assert right.data == []

    # 2D array
    a = Array([10, 20, 30, 40, 50, 60], (2, 3))

    left, pivot, right = partition(a, (1, 2))

    assert left.data == [10, 20, 30, 40, 50]
    assert pivot == 60
    assert right.data == []

    # 3D array
    a = Array([1, 2, 3, 4, 5, 6, 7, 8], (2, 2, 2))

    left, pivot, right = partition(a, (1, 0, 1))

    assert left.data == [1, 2, 3, 4, 5]
    assert pivot == 6
    assert right.data == [7, 8]
