"""Module containing all constants (e.g. Enums, Literals)    
"""

from typing import Literal, get_args


FileType = Literal["a", "b", "c", "d", "e", "f", "g", "h"]
RankType = Literal["1", "2", "3", "4", "5", "6", "7", "8"]
SideType = Literal["White", "Black"]
SquareColorType = Literal["Dark", "Light"]
GameModeType = Literal["Standard"]
    
FILES = get_args(FileType)
RANKS = get_args(RankType)
GAME_MODES = get_args(GameModeType)
SQUARE_COLORS = get_args(SquareColorType)