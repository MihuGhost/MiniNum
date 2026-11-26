
from mininum.array import Array

from mininum.linalg import (
    dot,
    matrix_add,
    transpose,
    matvec,
    matmul,
    identity,
    diagonal
)

def test_dot():
    # 1. Dot product
    a = Array([1, 2, 3], (3,))
    b = Array([4, 5, 6], (3,))

    assert dot(a, b) == 32

def test_matrix_add():
    # 2. Matrix addition
    A = Array([1, 2, 3, 4], (2, 2))
    B = Array([5, 6, 7, 8], (2, 2))

    C = matrix_add(A, B)

    assert C.data == [6, 8, 10, 12]
    assert C.shape == (2, 2)

def test_transpose():
    # 3. Transpose 1D
    A = Array([1, 2, 3], (3,))
    B = transpose(A)

    assert B.shape == (3,)
    assert B.data == [1, 2, 3]

    # 3. Transpose 2D
    A = Array([1, 2, 3, 4, 5, 6], (2, 3))
    B = transpose(A)

    assert B.shape == (3, 2)
    assert B.data == [1, 4, 2, 5, 3, 6]

    # 3. Transpose 3D
    A = Array(list(range(24)), (2, 3, 4))
    B = transpose(A)

    assert B.shape == (4, 3, 2)

    assert B.data == [
        0, 12, 4, 16, 8, 20,
        1, 13, 5, 17, 9, 21,
        2, 14, 6, 18, 10, 22,
        3, 15, 7, 19, 11, 23
    ]


def test_matvec():
    # 4. Matrix-vector multiplication
    A = Array([1, 2, 3, 4], (2, 2))
    v = Array([5, 6], (2,))

    C = matvec(A, v)

    assert C.data == [17, 39]
    assert C.shape == (2,)


def test_mulmat():
    # 5. Matrix-matrix multiplication
    A = Array([1, 2, 3, 4], (2, 2))
    B = Array([5, 6, 7, 8], (2, 2))

    C = matmul(A, B)

    assert C.data == [19, 22, 43, 50]
    assert C.shape == (2, 2)

def test_identity():
    # 6. Identity matrix
    I = identity(3)

    assert I.data == [
        1, 0, 0,
        0, 1, 0,
        0, 0, 1
    ]

    assert I.shape == (3, 3)


def test_diagonal():
    # 7. Diagonal extraction
    A = Array(
        [1, 2, 3,
         4, 5, 6,
         7, 8, 9],
        (3, 3)
    )

    d = diagonal(A)

    assert d.data == [1, 5, 9]
    assert d.shape == (3,)

