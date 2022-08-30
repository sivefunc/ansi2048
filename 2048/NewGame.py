from Graphics.GenGraphics import gen_graphics
from AddNewTile import add_new_tile

def new_game(parser_args, best_score=0):
    """
    Generate game default specs to start a new 2048 game
    """

    rows, columns, win_tile = parser_args[0:3]
    
    board = [[0] * columns for row in range(rows)]
    
    add_new_tile(board, [2], [100])
    add_new_tile(board, [2, 4], [90, 10])

    return [[0], 0, 0, 0, best_score, board, win_tile]
