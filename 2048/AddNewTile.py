from random import choice, choices

def add_new_tile(game_board, tiles_to_add, prob, repeat=1):
    """
    Add a random tile in a random X, Y Coordinate of the NxM Board
    If all squares are not empty nothing will happen
    """

    for i in range(repeat):
        blank_tiles = []
        for Y, tiles in enumerate(game_board):
            for X, tile in enumerate(tiles):
                if not tile:
                    blank_tiles.append([X, Y])

        if not blank_tiles: # Board not empty
            return False

        X,Y = choice(blank_tiles)
        game_board[Y][X] = choices(tiles_to_add, prob)[0]
