from .exceptions import ShapeError
from itertools import product


class Array:

    def __init__(self, data, shape):
        self._validate_shape(data, shape)

        self.data = data
        self.shape = tuple(shape)
        self.ndim = len(self.shape)
        self.size = len(self.data)
        self.strides = self._calculate_strides(self.shape)

    def __str__(self):
        return str(to_nested(self.data, self.shape))

    def __repr__(self):
        return f"Array({self.data}, shape={self.shape})"

    def __len__(self):
        return self.size

    def __getitem__(self, key):
        # Convert a single index into a tuple
        if not isinstance(key, tuple):
            key = (key,)

        # Check the number of indices
        if len(key) > self.ndim:
            raise IndexError("Too many indices")

        # Fill missing dimensions with full slices
        key = key + (slice(None),) * (self.ndim - len(key))

        selected_indices = []
        result_shape = []

        for axis, item in enumerate(key):
            # Integer indexing
            if isinstance(item, int) and not isinstance(item, bool):
                index = self._normalize_index(item, axis)
                selected_indices.append([index])
            # Slicing
            elif isinstance(item, slice):
                start, stop, step = item.indices(self.shape[axis])
                indices = list(range(start, stop, step))
                selected_indices.append(indices)
                result_shape.append(len(indices))
            else:
                raise TypeError("Invalid index type")

        # If every dimension uses integer indexing,
        # return a single element
        if not result_shape:
            indices = [
                selected_indices[i][0]
                for i in range(self.ndim)
            ]
            return self.data[self._flat_index(indices)]

        # Generate all selected multidimensional positions
        result_data = []
        for coordinates in product(*selected_indices):
            flat_index = self._flat_index(coordinates)
            result_data.append(self.data[flat_index])

        # Return a new Array containing the selected data
        return Array(result_data, tuple(result_shape))

    @staticmethod
    def _validate_shape(data, shape):
        # Check shape type
        if not isinstance(shape, (tuple, list)):
            raise TypeError("Shape must be a tuple or list.")

        # Check dimensions
        if not all(type(dim) is int for dim in shape):
            raise TypeError("Shape dimensions must be integers.")

        # Check negative dimensions
        if any(dim < 0 for dim in shape):
            raise ValueError("Shape dimensions cannot be negative.")

        # Check total number of elements
        expected_size = 1
        for dim in shape:
            expected_size *= dim

        if len(data) != expected_size:
            raise ValueError(
                f"Data size ({len(data)}) does not match "
                f"shape {shape} (expected {expected_size} elements)."
            )

    @staticmethod
    def _calculate_strides(shape):
        strides = [1] * len(shape)

        for i in range(len(shape) - 2, -1, -1):
            strides[i] = strides[i + 1] * shape[i + 1]

        return tuple(strides)

    def reshape(self, new_shape):
        # Calculate the expected number of elements
        expected_size = 1

        for dim in new_shape:
            expected_size *= dim

        # Validate the new shape
        if expected_size != self.size:
            raise ValueError("Cannot reshape array: size mismatch")

        self.shape = tuple(new_shape)
        self.ndim = len(self.shape)

    def copy(self):
        return Array(self.data.copy(), self.shape)

    def _normalize_index(self, index, axis):
        """Normalize positive and negative indices"""
        if not isinstance(index, int) or isinstance(index, bool):
            raise TypeError("Index must be an integer")

        if index < 0:
            index += self.shape[axis]

        if index < 0 or index >= self.shape[axis]:
            raise IndexError("Index out of bounds")

        return index

    # Convert multidimensional indices to flat index
    def _flat_index(self, indices):
        flat_index = 0

        for i in range(self.ndim):
            flat_index += indices[i] * self.strides[i]

        return flat_index


def to_nested(data, shape):
    if len(shape) == 1:
        return data

    step = 1
    for dim in shape[1:]:
        step *= dim

    return [
        to_nested(data[i:i + step], shape[1:])
        for i in range(0, len(data), step)
    ]
