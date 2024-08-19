"""Module containing exceptions
"""

class InvalidMoveError(Exception):
    """Error raised when an invalid move is attempted"""
    pass

class SelfCaptureError(Exception):
    """Error raised when a self-capture is attempted"""
    pass

class OutOfBoundsError(Exception):
    """Error raised when an index is out of bounds"""
    pass