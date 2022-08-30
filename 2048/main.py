import os
from sys import stdout

from Play import play
from NewGame import new_game
from GetKBChar import getch
from GameParser import game_parser
from NormalOrEnd import normal_or_end
from Verifiers.IsLegal import mvislegal
from Graphics.Exceptions.TermCantFitTXT import TermCantFitText

parser_args = [i for i in vars(game_parser()).values()]
write = stdout.write
ESC = chr(27)
CSI = ESC + '['

def main():
    
    os.system("clear") # Just one time, because it's slower better ANSI ESC SQ
    write(f'{CSI}?25l') # Hide cursor

    game_args = normal_or_end(new_game(parser_args, best_score=0), parser_args)
    while (key := getch()) and (board := game_args[5]): # Get keyboard input
        if key == ESC and getch() == '[' and (move := getch()):
            if move in {'A', 'B', 'C','D'}: # Arrow keys
                if mvislegal(board, mv := f'_{move}'):
                    game_args = normal_or_end(play(game_args, mv), parser_args)
        
        elif (key := key.upper()) in {'W', 'A', 'S', 'D', 'H', 'J', 'K', 'L'}:
            # Vim or Gaming KEY
            if mvislegal(board, key):
                game_args = normal_or_end(play(game_args, key), parser_args)
        
        elif key in {'Q', 'q'}:
            exit()

if __name__ == '__main__':
    try:

        main()
    
    except TermCantFitText as error:
        write(f'{CSI}0m')                           # Reset style and colors
        write(f'{CSI}{os.get_terminal_size()[0]}B') # Move cursor down
        write(f'{CSI}2J')                           # Erase entire screen
        write(f'{str(error)}\n')


    except KeyboardInterrupt: pass
    
    finally:
        write(f'{CSI}?25h')                         # Cursor visible
        write(f'{CSI}0m')                           # RST STY and COL
        write(f'{CSI}{os.get_terminal_size()[0]}B') # Move cursor down
        write(f'{CSI}2K')                           # Erase last line
