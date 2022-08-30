import copy
from Movements.MakeMovement import make_movement

def mvislegal(board1, move):
    
    """
    Verify if the given movement in the given NxM board makes an appreciated
    change in the board (If a tile changed of position or joins to other)
    """

    board2 = copy.deepcopy(board1)
    make_movement(board2, move)
    return board2 != board1


