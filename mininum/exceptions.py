class MiniNumError(Exception):
    """Base exception for MiniNum."""
    pass


class ShapeError(MiniNumError):
    """Raised when an array shape is invalid."""
    pass