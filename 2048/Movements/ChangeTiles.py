def change_tiles(
        game_board, blank_tiles,
        occupied_tile, X1, Y1, scores):

    """
    From a MxN board, move the tile if it's occupied and there's a blank
    tile available, if not the coordinate of tile will be put inside a list
    If it's a blank tile it will be append to blank_tiles if not it will 
    return the coordinate in a list called occupied_tile
    """

    if game_board[Y1][X1] == 0: # Blank tile
        blank_tiles.append([X1, Y1])

    else:
        if occupied_tile: # If there was a occupied tile
            X2, Y2 = occupied_tile
            if game_board[Y2][X2] == game_board[Y1][X1]:
                    # If are the same, e.g -> 2 and 2 make mv
                game_board[Y2][X2] *= 2
                game_board[Y1][X1] = 0
                blank_tiles.append([X1, Y1])
                occupied_tile.clear()
                scores.append(scores[-1] + game_board[Y2][X2])

            else: # Different tiles
                if blank_tiles: # If there was a blank tile make mv
                    X2, Y2 = blank_tiles.pop(0)
                    game_board[Y2][X2] = game_board[Y1][X1]
                    game_board[Y1][X1] = 0
                    blank_tiles.append([X1, Y1])
                    occupied_tile = [X2, Y2]
                
                else: # There wasn't a blank tile
                    occupied_tile = [X1, Y1]

        elif blank_tiles:
                # If there was a blank tile and not occupied tile
            X2, Y2 = blank_tiles.pop(0)
            game_board[Y2][X2] = game_board[Y1][X1]
            game_board[Y1][X1] = 0
            blank_tiles.append([X1, Y1])
            occupied_tile = [X2, Y2]

        else: # If there wasn't a blank tile or occupied tile
            occupied_tile = [X1, Y1]

    return occupied_tile
