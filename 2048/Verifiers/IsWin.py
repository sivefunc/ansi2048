def iswin(board, win_tile=-1):

    """
    Verify if the player has won the game by checking if win tile is on
    the given NxM board <Won't check if tile is greater than win tile>
    """

    return any([True for tiles in board if win_tile in tiles])
