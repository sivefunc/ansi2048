from .ChangeTiles import change_tiles

def move_up(board, scores=[0], column=0, row=0):
    """
    From a MxN board, move their tiles up going from the given column
    (def. 0) and given row (def. 0) and then increasing the row until
    get to the last row of the column and then increasing the column
    to repeat the process until get to the last column of the board
    """

    blank_tiles = []
    occupied_tile = []
    for X in range(column, len(board[0])):
        for Y in range(row, len(board)):
            occupied_tile = change_tiles(
                    board, blank_tiles,
                    occupied_tile, X, Y, scores)

        blank_tiles.clear()
        occupied_tile.clear()
