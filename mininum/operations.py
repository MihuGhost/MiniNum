from .array import Array
from .exceptions import ShapeError
from numbers import Number
from operator import (
    add,
    sub,
    mul,
    truediv,
    eq,
    ne,
    lt,
    le,
    gt,
    ge,
)

def _binary_operation(a, b, operation):
    """
    Apply an element-wise operation to two arrays
    or an array and a scalar.
    """
    # Array with Array
    if isinstance(a, Array) and isinstance(b, Array):
        # broadcast shape

        #index mapping

        if a.shape != b.shape:
            raise ShapeError(
                f"Shape mismatch: {a.shape} and {b.shape}"
            )

        result = [
            operation(x, y)
            for x, y in zip(a.data, b.data)
        ]

        return Array(result, a.shape)

    # Array with scalar
    if isinstance(a, Array) and isinstance(b, Number):
        result = [
            operation(x, b)
            for x in a.data
        ]

        return Array(result, a.shape)

    # Scalar with Array
    if isinstance(a, Number) and isinstance(b, Array):
        result = [
            operation(a, x)
            for x in b.data
        ]

        return Array(result, b.shape)

    raise TypeError(
        "Operands must be Array objects or numeric scalars."
    )


# Arithmetic operations

def add_arrays(a, b):
    return _binary_operation(a, b, add)


def subtract_arrays(a, b):
    return _binary_operation(a, b, sub)


def multiply_arrays(a, b):
    return _binary_operation(a, b, mul)


def divide_arrays(a, b):
    return _binary_operation(a, b, truediv)


# Element-wise comparisons

def equal(a, b):
    return _binary_operation(a, b, eq)


def not_equal(a, b):
    return _binary_operation(a, b, ne)


def less_than(a, b):
    return _binary_operation(a, b, lt)


def less_equal(a, b):
    return _binary_operation(a, b, le)


def greater_than(a, b):
    return _binary_operation(a, b, gt)


def greater_equal(a, b):
    return _binary_operation(a, b, ge)




def broadcast_shape(shape_a, shape_b):

    max_ndim = max(len(shape_a), len(shape_b))

    # Pad the shorter shape with leading ones
    shape_a = (1,) * (max_ndim - len(shape_a)) + shape_a
    shape_b = (1,) * (max_ndim - len(shape_b)) + shape_b

    result = []

    for dim_a, dim_b in zip(shape_a, shape_b):

        if dim_a == dim_b:
            result.append(dim_a)

        elif dim_a == 1:
            result.append(dim_b)

        elif dim_b == 1:
            result.append(dim_a)

        else:
            raise ValueError(
                f"Cannot broadcast {shape_a} and {shape_b}"
            )

    return tuple(result)
