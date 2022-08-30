from .ChangeTiles import change_tiles

def move_left(board, scores=[0], column=0, row=0):
    """
    From a MxN board, move their tiles right going from the given row
    (def. 0) and given column (def. 0) and then increasing the column
    until get to the last column of the row and then increasing the row
    to repeat the process until get to the last row of the board
    """

    blank_tiles = []
    occupied_tile = []
    for Y in range(row, len(board)):
        for X in range(column, len(board[Y])):
            occupied_tile = change_tiles(
                    board, blank_tiles,
                    occupied_tile, X, Y, scores)
        
        blank_tiles.clear()
        occupied_tile.clear()
