from Movements.MakeMovement import make_movement
from AddNewTile import add_new_tile

def play(game_args, move):
    """
    Play the given move using the current specs of the game return a modified
    game specs
    """

    [all_scores, old_score, new_score,
    score_added, best_score, board, win_tile] = game_args # Unpack game specs
    
    old_score = new_score
    
    make_movement(board, move, all_scores)
    add_new_tile(board, [2, 4], [90, 10]) # 10% to get a tile with value 4
    if old_score != (new_score := all_scores[-1]): # If a tile wasn't added
        if new_score > best_score: # Total score broke the record
            best_score = new_score
        score_added = new_score - old_score # check how much was added
    
    return [all_scores, old_score, new_score, score_added,
                best_score, board, win_tile]
