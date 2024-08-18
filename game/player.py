"""
Module containing abstract Player class and all specific player classes
"""

from constants import SideType
from abc import ABC


class Player(ABC):
    """
    Abstract player class
    """
    def __init__(self, side: SideType) -> None:
        self.side = side
        self.captured_pieces = []