from itertools import repeat
from Verifiers.IsLegal import mvislegal


def islose(board):
    """
    Verify if the player losed the game checking if the player can't move
    """

    return not any(map(mvislegal, repeat(board), ['W','A','S','D']))
