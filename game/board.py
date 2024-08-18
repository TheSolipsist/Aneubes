"""
Board module containing square and board classes
"""

from constants import FileType, RankType, SquareColorType, GameModeType
from constants import FILES, RANKS


class Square:
    """
    Square class
    """
    def __init__(self, file: FileType, rank: RankType) -> None:
        self.file = file
        self.rank = rank
        self.occupied_by: "Piece" = None
        self.color: SquareColorType = None
        
        
class Board:
    """
    Board class
    """
    def __init__(self, mode: GameModeType):
        self.mode = mode
        self.squares = []
        if mode == "Standard":
            self._setup_standard_board()
        
    def _setup_standard_board(self):
        self.squares = [Square(i, j) for i in FILES for j in RANKS]