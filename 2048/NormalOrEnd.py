from Graphics.GenGraphics import gen_graphics
from EndOfGame import end_of_game
from Verifiers.IsLose import islose
from Verifiers.IsWin import iswin

def normal_or_end(game_args, parser_args):
    """
    Check the status of the NxM board to know if it's in end state or
    normal mode
    """

    board, win_tile = game_args[-2:]
    if (is_win := iswin(board, win_tile)) | (is_lose := islose(board)):
        # Check if movement caused the end state of NxM board
        game_args = end_of_game(game_args, parser_args, is_win, is_lose)

    gen_graphics(game_args, parser_args)
    
    game_args[3] = 0 # Reset score added
    return game_args
