from .exceptions import ShapeError

class Array:

    def __init__(self, data, shape):
        flat_data = flatten(data)

        self._validate_shape(data, shape)

        self.data = data
        self.shape = tuple(shape)
        self.ndim = len(self.shape)
        self.size = len(self.data)

    def __str__(self):
        return str(to_nested(self.data, self.shape))

    def __repr__(self):
        return f"Array({self.data}, shape={self.shape})"

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

def flatten(data):
    result = []

    for item in data:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

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



