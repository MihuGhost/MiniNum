from .array import Array
from itertools import product
from numbers import Number


def ravel_index(index, shape):
    """
    Convert multidimensional coordinates into a flat index.
    """
    flat_index = 0

    for i, dim in zip(index, shape):
        flat_index = flat_index * dim + i

    return flat_index


def elementwise_operation(a, b, operation):
    # CASE 1: Array + Array
    if isinstance(a, Array) and isinstance(b, Array):

        # Situation 1: Same shapes
        if a.shape == b.shape:
            result = [
                operation(x, y)
                for x, y in zip(a.data, b.data)
            ]

            return Array(result, a.shape)

        # Situation 2: Different shapes (Broadcasting)

        # Step 1: Align dimensions
        ndim = max(len(a.shape), len(b.shape))

        aligned_a = (1,) * (ndim - len(a.shape)) + a.shape
        aligned_b = (1,) * (ndim - len(b.shape)) + b.shape

        # Step 2: Determine broadcast shape
        result_shape = []

        for dim_a, dim_b in zip(aligned_a, aligned_b):

            if dim_a == dim_b:
                result_shape.append(dim_a)

            elif dim_a == 1:
                result_shape.append(dim_b)

            elif dim_b == 1:
                result_shape.append(dim_a)

            else:
                raise ValueError(
                    f"Cannot broadcast {a.shape} and {b.shape}"
                )

        result_shape = tuple(result_shape)

        # Step 3: Generate output coordinates
        result = []

        for output_index in product(
                *(range(dim) for dim in result_shape)
        ):
            # Step 4: Map output coordinates to A
            index_a = tuple(
                0 if dim == 1 else idx
                for idx, dim in zip(output_index, aligned_a)
            )

            # Step 5: Map output coordinates to B
            index_b = tuple(
                0 if dim == 1 else idx
                for idx, dim in zip(output_index, aligned_b)
            )

            # Step 6: Remove artificial leading dimensions
            original_index_a = index_a[ndim - len(a.shape):]
            original_index_b = index_b[ndim - len(b.shape):]

            # Step 7: Convert coordinates to flat indices
            flat_a = ravel_index(original_index_a, a.shape)
            flat_b = ravel_index(original_index_b, b.shape)

            # Step 8: Perform operation
            result.append(
                operation(a.data[flat_a], b.data[flat_b])
            )

        return Array(result, result_shape)

    # CASE 2: Array + Scalar
    elif isinstance(a, Array) and isinstance(b, Number):

        result = [
            operation(x, b)
            for x in a.data
        ]

        return Array(result, a.shape)

    # CASE 3: Scalar + Array
    elif isinstance(a, Number) and isinstance(b, Array):

        result = [
            operation(a, y)
            for y in b.data
        ]

        return Array(result, b.shape)

    else:
        raise TypeError("Operands must be Array or numeric scalar")


def add(a, b):
    return elementwise_operation(a, b, lambda x, y: x + y)


def subtract(a, b):
    return elementwise_operation(a, b, lambda x, y: x - y)


def multiply(a, b):
    return elementwise_operation(a, b, lambda x, y: x * y)


def divide(a, b):
    return elementwise_operation(a, b, lambda x, y: x / y)


def equal(a, b):
    return elementwise_operation(a, b, lambda x, y: x == y)


def not_equal(a, b):
    return elementwise_operation(a, b, lambda x, y: x != y)


def less_than(a, b):
    return elementwise_operation(a, b, lambda x, y: x < y)


def less_equal(a, b):
    return elementwise_operation(a, b, lambda x, y: x <= y)


def greater_than(a, b):
    return elementwise_operation(a, b, lambda x, y: x > y)


def greater_equal(a, b):
    return elementwise_operation(a, b, lambda x, y: x >= y)
