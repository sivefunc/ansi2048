from Graphics.GenGraphics import gen_graphics
from NewGame import new_game
from GetKBChar import getch

def end_of_game(
        game_args, parser_args,
        is_win, is_lose):
    
    """
    The NxM board reach it's possible end state when the max tile
    is in the board or the tiles can't move, Now the player has to
    choose between two buttons <Continue> or <Exit>
    """

    button = [1, 0] # Left button on <Continue>, Right button off <Exit>
    gen_graphics(game_args, parser_args, button, is_win, is_lose)

    while (key := getch()) and not (enter_key := False):
        if key == chr(27) and getch() == '[' and (mv := getch()) in {'C', 'D'}:
            button = [0, 1] if mv == 'C' else [1, 0] # Change button state
    
        elif (key := key.upper()) in {'H', 'L', 'A', 'D'}:
            button = [0, 1] if key in {'L', 'D'} else [1, 0] # Change button
        
        elif key == '\n':
            enter_key = True # Button pressed

        elif key in {'Q', 'q'}:
            exit() # Quit the game
        
        else:
            continue # Key unknown
        
        gen_graphics(game_args, parser_args, button, is_win, is_lose)

        if button == [0, 1] and enter_key:
            exit() # Pressed exit button
        
        elif button == [1, 0] and enter_key: # Pressed continue button
            if is_lose:
                game_args = new_game(parser_args, game_args[4])

            else:
                game_args[-1] = -1 # There's no tile limit now
            
            return game_args