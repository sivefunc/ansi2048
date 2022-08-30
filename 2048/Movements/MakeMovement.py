from .MoveUp import move_up
from .MoveDown import move_down
from .MoveLeft import move_left
from .MoveRight import move_right

moves = {
        # Arrow keys        # Gaming keys       # Vim keys
        '_A': move_up,      'W': move_up,       'K': move_up,
        '_B': move_down,    'S': move_down,     'J': move_down,
        '_C': move_right,   'D': move_right,    'L': move_right,
        '_D': move_left,    'A': move_left,     'H': move_left,
        }

def make_movement(board, move, scores=[0]):
    """
    Makes movement
    """

    moves[move](board, scores)
