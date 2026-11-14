import pytest
from mininum import Array

""""
PHASE 1
"""

def test_invalid_shape():
    with pytest.raises(
            ValueError,
            match="Data size"
    ):
        Array([1, 2, 3], (2, 2))


def test_negative_shape():
    with pytest.raises(
            ValueError,
            match="negative"
    ):
        Array([1, 2], (-1, 2))


def test_invalid_shape_type():
    with pytest.raises(
            TypeError,
            match="a tuple or list"
    ):
        Array([1, 2], "2, 1")


def test_invalid_shape_dimensions():
    with pytest.raises(
            TypeError,
            match="integers"
    ):
        Array([1, 2], ("a", 2))


def test_reshape():
    arr = Array([1, 2, 3, 4, 5, 6], (2, 3))
    arr.reshape((3, 2))
    assert arr.shape == (3, 2)
    assert arr.ndim == 2
    assert arr.size == 6
    assert arr.strides == (3, 1)
    assert arr.data == [1, 2, 3, 4, 5, 6]


def test_reshape_invalid_size():
    arr = Array([1, 2, 3, 4], (2, 2))

    with pytest.raises(ValueError):
        arr.reshape((3, 2))


def test_copy():
    arr1 = Array([1, 2, 3, 4], (2, 2))

    arr2 = arr1.copy()

    assert arr2.data == arr1.data
    assert arr2.shape == arr1.shape

    # They should be different objects
    assert arr2 is not arr1

    # Their data lists should also be independent
    assert arr2.data is not arr1.data


def test_str():
    arr = Array([1, 2, 3, 4], (2, 2))

    assert str(arr) == "[[1, 2], [3, 4]]"


def test_repr():
    arr = Array([1, 2, 3, 4], (2, 2))

    assert repr(arr) == "Array([1, 2, 3, 4], shape=(2, 2))"


def test_array_definition():
    arr = Array([1, 2, 3, 4], (2, 2))
    assert len(arr) == 4


"""
PHASE 2
"""

def test_array_indexing():
    arr = Array(
        [10, 20, 30, 11, 21, 31, 40, 50, 60, 41, 51, 61,
         101, 201, 301, 111, 211, 311, 401, 501, 601, 411, 511, 611],
        (2, 3, 2, 2)
    )
    # 1. Row extraction
    # 2. positive indexing
    first = arr[0]
    # negative indexing
    second = arr[-1]
    assert first.shape == (3, 2, 2,)
    assert second.shape == (3, 2, 2,)
    assert first.data == arr.data[:12]
    assert second.data == arr.data[12:]

    # 3. Bounds checks
    with pytest.raises(
            IndexError,
            match="bounds"
    ): var = arr[1, 2, 1, 2]

    # 4. Multidimensional indexing
    assert arr.data[16] == arr[1, 1, 0, 0]
    assert arr.data[23] == arr[1, 2, 1, 1]

    # 5. Basic slicing
    s1 = arr[0, 1:3]
    assert s1.shape == (2, 2, 2)
    assert s1.data == arr.data[4:12]
    s2 = arr[0, 1:]
    assert s2.shape == (2, 2, 2)
    assert s2.data == arr.data[4:12]

    # 6. Column extraction
    col = arr[:, :, 1, :]
    assert col.shape == (2, 3, 2)
    assert (col.data == arr.data[2:4] + arr.data[6:8] + arr.data[10:12] +
            arr.data[14:16] + arr.data[18:20] + arr.data[
                22:24])

def test_copying_view_slice():
    arr = Array([10, 20, 30, 40, 50], (5,))
    sliced = arr[1:4]
    sliced.data[0] = 999
    assert arr.data == [10, 20, 30, 40, 50]
    assert sliced.data == [999, 30, 40]
