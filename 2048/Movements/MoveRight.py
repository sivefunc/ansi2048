from .ChangeTiles import change_tiles

def move_right(board, scores=[0], column=-1, row=0):
    """
    From a MxN board, move their tiles right going from the given row
    (def. 0) and given column (def. -1) and then increasing by -1 the
    column until get to the first column of the row and then increasing
    the row to repeat the process until get to the last row of the board
    """
    
    blank_tiles = []
    occupied_tile = []
    for Y in range(row, len(board)):
        for X in range(column, -(len(board[Y]) + 1), -1):
            occupied_tile = change_tiles(
                    board, blank_tiles,
                    occupied_tile, X, Y, scores)

        blank_tiles.clear()
        occupied_tile.clear()
