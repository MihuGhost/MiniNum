from .array import Array
from itertools import product
from numbers import Number

from .exceptions import ShapeError


def elementwise_operation(a, b, operation):
    a, b = broadcast_shape(a, b)

    result = [
        operation(x, y)
        for x, y in zip(a.data, b.data)
    ]

    return Array(result, a.shape)


def broadcast_shape(a, b):
    # Case 1: scalar and array
    if isinstance(a, Number) and isinstance(b, Array):
        a = Array([a] * len(b.data), b.shape)
        return a, b

    if isinstance(a, Array) and isinstance(b, Number):
        b = Array([b] * len(a.data), a.shape)
        return a, b

    # Case 2: two arrays
    if isinstance(a, Array) and isinstance(b, Array):

        if a.shape == b.shape:
            return a, b

        ndim = max(len(a.shape), len(b.shape))

        aligned_a = (1,) * (ndim - len(a.shape)) + a.shape
        aligned_b = (1,) * (ndim - len(b.shape)) + b.shape

        result_shape = []

        for dim_a, dim_b in zip(aligned_a, aligned_b):
            if dim_a == dim_b:
                result_shape.append(dim_a)
            elif dim_a == 1:
                result_shape.append(dim_b)
            elif dim_b == 1:
                result_shape.append(dim_a)
            else:
                raise ShapeError(
                    f"Cannot broadcast {a.shape} and {b.shape}"
                )

        result_shape = tuple(result_shape)

        new_a = broadcast_to(a, result_shape, aligned_a)
        new_b = broadcast_to(b, result_shape, aligned_b)

        return new_a, new_b

    raise TypeError("Operands must be Arrays or numbers")


def broadcast_to(array, target_shape, aligned_shape):
    result = []

    for output_index in product(
            *(range(dim) for dim in target_shape)
    ):
        input_index = tuple(
            0 if old_dim == 1 else output_dim
            for old_dim, output_dim in zip(aligned_shape, output_index)
        )

        # Remove the leading dimensions added during alignment
        input_index = input_index[len(aligned_shape) - len(array.shape):]

        flat_index = ravel_index(input_index, array.shape)

        result.append(array.data[flat_index])

    return Array(result, target_shape)


def ravel_index(index, shape):
    """Convert a multidimensional index to a flat index."""
    flat_index = 0

    for i, dim in zip(index, shape):
        flat_index = flat_index * dim + i

    return flat_index


def add(a, b):
    return elementwise_operation(a, b, lambda x, y: x + y)


def subtract(a, b):
    return elementwise_operation(a, b, lambda x, y: x - y)


def multiply(a, b):
    return elementwise_operation(a, b, lambda x, y: x * y)


def divide(a, b):
    return elementwise_operation(a, b, lambda x, y: x / y)


def equal(a, b):
    if not isinstance(b, Array):
        return False

    return a.data == b.data and a.shape == b.shape


def not_equal(a, b):
    return not equal(a, b)


def less_than(a, b):
    return elementwise_operation(a, b, lambda x, y: x < y)


def less_equal(a, b):
    return elementwise_operation(a, b, lambda x, y: x <= y)


def greater_than(a, b):
    return elementwise_operation(a, b, lambda x, y: x > y)


def greater_equal(a, b):
    return elementwise_operation(a, b, lambda x, y: x >= y)
