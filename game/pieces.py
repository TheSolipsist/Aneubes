"""Module containing the abstract Piece class and all specific piece classes
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Piece(ABC):
    """Abstract base class for chess pieces."""
    
    def __init__(self, starting_square: "Square", player: "Player") -> None:
        self.square = starting_square
        self.player = player
    
    def move(
            self, 
            destination_square: "Square", 
            skip_validity_check: bool = False
        ) -> bool:
        """Attempts to move to "destination_square", capturing any pieces that
        are there if the move was valid.

        Args:
            destination_square (Square): Move's destination square
            skip_validity_check (bool): Specifies if validity check should be 
                                        skipped.
                                        **WARNING**: Undefined behavior if move
                                        was invalid.
                
        Returns:
            bool: True if attempted move was valid (and executed), False if
                invalid.
        """
        if skip_validity_check or self.is_valid_move(destination_square):
            self._perform_move(destination_square)
            return True
        else:
            return False
    
    def _perform_move(self, destination_square: "Square") -> None:
        self.square.occupied_by = None
        self.square = destination_square
        if destination_square.occupied_by is not None:
            self.player.captured_pieces.append(destination_square.occupied_by)
        destination_square.occupied_by = self
        
    @abstractmethod
    def is_valid_move(self, destination_square: "Square") -> bool:
        """
        Checks whether a move to the "destination_square" is valid. 
        
        This method should be implemented by subclasses of the Piece class 
            with specific validation logic, depending on the piece's movement
            rules.

        Args:
            destination_square (Square): Attempted move's destination square.

        Returns:
            bool: True if attempted move was valid (and executed), False 
                if invalid.
        """
        pass


class Pawn(Piece):
    """Represents a pawn piece.
    
    A pawn can only move forward one square, or capture on its diagonally
    adjacent square"""
    
    def __init__(self, starting_square: "Square", player: "Player"):
        super().__init__(starting_square, player)
        
    def is_valid_move(self, destination_square: "Square") -> bool:
        pass


class Rook(Piece):
    """Represents a rook piece."""
    
    def __init__(self, starting_square: "Square", player: "Player"):
        super().__init__(starting_square, player)
        
    def is_valid_move(self, destination_square: "Square") -> bool:
        pass
    
    
class Knight(Piece):
    """Represents a knight piece."""
    
    def __init__(self, starting_square: "Square", player: "Player"):
        super().__init__(starting_square, player)
        
    def is_valid_move(self, destination_square: "Square") -> bool:
        pass
    
    
class Bishop(Piece):
    """Represents a bishop piece."""
    
    def __init__(self, starting_square: "Square", player: "Player"):
        super().__init__(starting_square, player)
        
    def is_valid_move(self, destination_square: "Square") -> bool:
        pass
    
    
class Queen(Piece):
    """Represents a queen piece."""
    
    def __init__(self, starting_square: "Square", player: "Player"):
        super().__init__(starting_square, player)
        
    def is_valid_move(self, destination_square: "Square") -> bool:
        pass
    
    
class King(Piece):
    """Represents a king piece."""
    
    def __init__(self, starting_square: "Square", player: "Player"):
        super().__init__(starting_square, player)
        
    def is_valid_move(self, destination_square: "Square") -> bool:
        pass
