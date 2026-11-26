import itertools
from .array import Array

def _check_vector(a):
    """Check whether an array is a 1D vector."""
    if len(a.shape) != 1:
        raise ValueError("Expected a 1D vector")

def _check_matrix_2d(A):
    """Check that the input is a two-dimensional array."""
    if len(A.shape) != 2:
        raise ValueError("Expected a two-dimensional matrix")

# ==================================================
# 1. Vector Dot Product
# ==================================================

def dot(a, b):
    """Compute the dot product of two vectors."""
    _check_vector(a)
    _check_vector(b)

    if a.shape[0] != b.shape[0]:
        raise ValueError("Vectors must have the same length")

    result = 0

    for i in range(a.shape[0]):
        result += a.data[i] * b.data[i]

    return result


# ==================================================
# 2. Matrix Addition
# ==================================================

def matrix_add(A, B):
    if A.shape != B.shape:
        raise ValueError("Matrices must have the same shape")

    result = []

    for i in range(len(A.data)):
        result.append(A.data[i] + B.data[i])

    return Array(result, A.shape)


# ==================================================
# 3. N-dimensional Transpose
# ==================================================

def transpose(A, axes=None):
    """
    Transpose an N-dimensional Array.

    Default:
        Reverse the order of axes.

    Examples:
        (2, 3)    -> (3, 2)
        (2, 3, 4) -> (4, 3, 2)

    axes:
        Optional permutation of dimensions.

    Time complexity: O(N*d)
    N = number of elements
    d = number of dimensions
    """

    ndim = len(A.shape)

    # Default: reverse all axes
    if axes is None:
        axes = tuple(reversed(range(ndim)))
    else:
        axes = tuple(axes)

    # Calculate the new shape
    new_shape = tuple(A.shape[i] for i in axes)

    result = []

    # Generate all output indices
    output_indices = itertools.product(
        *(range(dim) for dim in new_shape)
    )

    for out_idx in output_indices:

        # Map output indices to input indices
        input_idx = [0] * ndim

        for out_axis, in_axis in enumerate(axes):
            input_idx[in_axis] = out_idx[out_axis]

        # Convert input coordinates to flat index
        flat_index = 0

        for i in range(ndim):
            flat_index = (
                    flat_index * A.shape[i] + input_idx[i]
            )

        result.append(A.data[flat_index])

    return Array(result, new_shape)


# ==================================================
# 4. Matrix-Vector Multiplication
# ==================================================

def matvec(A, v):
    """
    Multiply a matrix by a vector.

    A: (m, n)
    v: (n,)

    Returns: (m,)

    Time complexity: O(m*n)
    """

    _check_matrix_2d(A)
    _check_vector(v)

    rows, cols = A.shape

    if cols != v.shape[0]:
        raise ValueError(
            "Matrix columns must equal vector length"
        )

    result = []

    for i in range(rows):
        total = 0

        for j in range(cols):
            index = i * cols + j
            total += A.data[index] * v.data[j]

        result.append(total)

    return Array(result, (rows,))


# ==================================================
# 5. Matrix-Matrix Multiplication for 2D
# ==================================================

def matmul(A, B):
    """
    Multiply two matrices.

    A: (m, k)
    B: (k, n)

    Returns: (m, n)

    Time complexity: O(m*k*n)
    """

    _check_matrix_2d(A)
    _check_matrix_2d(B)

    m, k = A.shape
    k2, n = B.shape

    if k != k2:
        raise ValueError(
            "Incompatible matrix dimensions"
        )

    result = [0] * (m * n)

    for i in range(m):

        for j in range(n):

            total = 0

            for r in range(k):
                a_index = i * k + r
                b_index = r * n + j

                total += (
                        A.data[a_index] * B.data[b_index]
                )

            result[i * n + j] = total

    return Array(result, (m, n))


# ==================================================
# 6. Identity Matrix Construction
# ==================================================

def identity(n):
    """
    Construct an n x n identity matrix.

    Returns: (n, n)

    Time complexity: O(n^2)
    """

    if not isinstance(n, int) or isinstance(n, bool) or n < 0:
        raise ValueError("Matrix size must be a non-negative integer")

    result = [0] * (n * n)

    for i in range(n):
        result[i * n + i] = 1

    return Array(result, (n, n))


# ==================================================
# 7. Diagonal Extraction for 2d
# ==================================================

def diagonal(A):
    """
    Extract the main diagonal of a matrix.

    A: (m, n)

    Returns: (min(m, n),)

    Time complexity: O(min(m, n))
    """
    _check_matrix_2d(A)

    rows, cols = A.shape

    length = min(rows, cols)

    result = []

    for i in range(length):
        index = i * cols + i
        result.append(A.data[index])

    return Array(result, (length,))
