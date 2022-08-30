from .ChangeTiles import change_tiles

def move_down(board, scores=[0], column=0, row=-1):
    """
    From a MxN board, move their tiles up going from the given column
    (def. 0) and given row (def. -1) and then increasing ny -1 the row
    until get to the first row of the column and then increasing the column
    to repeat the process until get to the last column of the board
    """
    
    blank_tiles = []
    occupied_tile = []
    for X in range(len(board[0])):
        for Y in range(row, -(len(board) + 1), -1):
            occupied_tile = change_tiles(
                    board, blank_tiles,
                    occupied_tile, X, Y, scores)

        blank_tiles.clear()
        occupied_tile.clear()
