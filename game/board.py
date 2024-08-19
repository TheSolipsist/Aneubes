"""Board module containing square and board classes
"""

from __future__ import annotations

from typing import overload

from constants import FileType, RankType, SquareColorType, GameModeType
from constants import FILES, RANKS, SQUARE_COLORS


class Square:
    """Represents a square on the chess board.
    
    Attributes:
        coords (tuple[int, int]): The square's numerical coordinates.
        occupied_by (Piece | None): The piece currently on the square.
        file (FileType): The square's file (column), e.g. "c".
        rank (RankType): The square's rank (row), e.g. "3".
        color (SquareColorType): The square's color (Light, Dark).
    """
    
    def __init__(self, file: FileType, rank: RankType) -> None:
        """Initializes a square with a file and a rank.

        Args:
            file (FileType): The square's file (column), e.g. "c".
            rank (RankType): The square's rank (row), e.g. "3".
        """
        self._file: FileType = file
        self._rank: RankType = rank
        self._coords: tuple[int, int] = (FILES.index(file), RANKS.index(rank))
        self._occupied_by: "Piece" = None
        self._color: SquareColorType = SQUARE_COLORS[(sum(self._coords)) % 2]
    
    @property
    def coords(self) -> tuple[int, int]:
        """The square's numerical rank-major coordinates 
        
        Example: 
            Square "a4" -> (0, 3))
        """
        return self._coords
    
    @property
    def occupied_by(self) -> "Piece" | None:
        """The piece currently on the square (None if no piece on square)."""
        return self._occupied_by
    
    @occupied_by.setter
    def occupied_by(self, piece: "Piece" | None):
        self._occupied_by = piece
    
    @property
    def file(self) -> FileType:
        """The square's file (column)."""
        return self._file

    @property
    def rank(self) -> RankType:
        """The square's rank (row)."""
        return self._rank
    
    @property
    def color(self) -> SquareColorType:
        """The square's color ("Light" or "Dark")."""
        return self._color
    
    def __str__(self) -> str:
        """Returns a human-readable form of the square, e.g. 'a4'."""
        return self.file + self.rank
    
    def __repr__(self) -> str:
        return self.file + self.rank
        
        
class Board:
    """Represents the chess board.
    
    Attributes:
        mode (GameModeType): The game mode to be played.
        files (list[list[Square]]): A list of the board's files.
        ranks (list[list[Square]]): A list of the board's ranks.
    """
    
    def __init__(self, mode: GameModeType = "Standard"):
        """Initializes the board for a particular game mode.

        Args:
            mode (GameModeType): The game mode to be played.
        """
        self.mode: GameModeType = mode
        self._squares: list[list[Square]] = [[]]
        self._files: list[list[Square]] = [[]]
        self._ranks: list[list[Square]] = [[]]
        if mode == "Standard":
            self._setup_standard_board()
    
    @property
    def files(self) -> list[list[Square]]:
        """A list of the board's files"""
        return self._files
    
    @property
    def ranks(self) -> list[list[Square]]:
        """A list of the board's ranks"""
        return self._ranks
    
    @overload
    def __getitem__(self, key: slice[int]) -> list[Square] | list[list[Square]]: ...
    @overload
    def __getitem__(self, key: int) -> list[Square]: ...
    @overload
    def __getitem__(self, key: tuple[int]) -> Square: ...
    def __getitem__(
        self, 
        key: slice[int] | int | tuple[int]
    ) -> Square | list[Square] | list[list[Square]]:
        if isinstance(key, tuple):
            print(key[0])
            return self._squares[key[0]][key[1]]
        elif isinstance(key, int):
            return self._files[key]
        elif isinstance(key, slice):
            return self._squares[key]
        else:
            raise TypeError("key can only be tuple[int], int, or slice[int]")
        
    def _setup_standard_board(self):
        """Sets up the board for standard chess"""
        self._squares = [[Square(file, rank) for rank in RANKS] for file in FILES]
        self._files = self._squares # self._squares is rank-major, therefore
        # self._squares[i] returns the i-th file
        self._ranks = [
            [self._squares[i][j] for i in range(len(self._squares))]
            for j in range(len(self._squares[0]))
        ]
