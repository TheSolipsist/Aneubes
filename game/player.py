"""
Module containing abstract Player class and all specific player classes
"""

from __future__ import annotations

from constants import SideType
from exceptions import SelfCaptureError

from abc import ABC


class Player(ABC):
    """Abstract base class representing a player.
    
    Attributes:
        side (SideType): The player's side (White or Black in standard mode).
        captured_pieces (list[Piece]): Pieces that the player has captured.
    
    Methods:
        capture (piece: Piece): Captures another player's piece
    """
    
    def __init__(self, side: SideType) -> None:
        self._side: SideType = side
        self._captured_pieces: list["Piece"] = []
        
    @property
    def side(self) -> SideType:
        """The player's side (White or Black in standard mode)"""
        return self._side
    
    @property
    def captured_pieces(self) -> list("Piece"):
        """All the pieces that the player has captured"""
        return self._captured_pieces

    def capture(self, piece: "Piece") -> None:
        """Captures a piece, adding it to the list of captured pieces.
        
        Args:
            piece (Piece): The piece to be captured.
        
        Raises:
            SelfCaptureError: The player attempted to capture his own piece
        """
        if piece.player is self:
            raise SelfCaptureError(
                f"Player {self} attempted to capture his "
                f"own piece {piece}"
            )
        self.captured_pieces.append(piece)