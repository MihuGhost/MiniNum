import pytest
from mininum import Array
from mininum.array import flatten

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
        Array([1, 2], ("a",2))

def test_flatten_1d():
    data = [1,2,3,4]
    assert flatten(data) == data

def test_flatten_3d():
    data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
    assert flatten(data) == [1, 2, 3, 4, 5, 6, 7, 8]

def test_reshape():
    arr = Array([1, 2, 3, 4, 5, 6], (2, 3))
    arr.reshape((3, 2))
    assert arr.shape == (3, 2)
    assert arr.ndim == 2
    assert arr.size == 6
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


