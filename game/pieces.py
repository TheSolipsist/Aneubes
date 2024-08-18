"""
Module containing the abstract Piece class and all specific piece classes
"""

from abc import ABC, abstractmethod

        
class Piece(ABC):
    """
    Abstract piece class
    """
    def __init__(self, starting_square: "Square", player: "Player") -> None:
        self.square = starting_square
        self.player = player
    
    def move(self, destination_square: "Square", skip_validity_check: bool = False) -> bool:
        """
        Attempts to move to "destination_square", capturing any pieces that are there if the move was valid.

        Args:
            destination_square (Square): Move's destination square
            skip_validity_check (bool): Specifies if validity check should be skipped
                                        **WARNING** undefined behavior if move was invalid
                
        Returns:
            bool: True if attempted move was valid (and executed), False if invalid
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
        
        This method should be implemented by subclasses of the Piece class with specific validation
        logic, depending on the piece's movement rules.

        Args:
            destination_square (Square): Attempted move's destination square

        Returns:
            bool: True if attempted move was valid (and executed), False if invalid
        """
        pass
    