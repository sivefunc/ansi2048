import os
from sys import stdout

from Graphics.Exceptions.TermCantFitTXT import TermCantFitText
from Graphics.BottomText.GenBottomText import gen_bottom_text
from Graphics.GameInfo.GenGameInfo import gen_game_info
from Graphics.GenGameBoard import gen_game_board
from Graphics.GameColors import bg_color


ESC = chr(27)
CSI = ESC + '['
write = stdout.write

def gen_graphics(
        game_args, parser_args, buttons_options=[0,0],
        is_win=False, is_lose=False):
    
    new_score, score_added, best_score, board = game_args[2:-1]
    hor_pad, ver_pad, tile_rows_n, tile_columns_n, lang, bitd = parser_args[3:]

    write(bg_color[bitd] + f'{CSI}2J{CSI}H') # Fill screen with bg
    term_columns, term_rows = os.get_terminal_size()    
    
    score_added = f'+{score_added}' if score_added else ''
    
    GAME_INFO = gen_game_info(
            term_columns, term_rows, lang,
            str(new_score), score_added, str(best_score),
            bitd)

    RTX_BOARD = gen_game_board(
            board, term_columns, term_rows,
            tile_rows_n, tile_columns_n,
            hor_pad, ver_pad, bitd)
    
    ver_lines = (tile_rows_n * len(board) + len(board) * ver_pad + ver_pad
                + len(GAME_INFO))

    UP_SPACES = int((term_rows - (ver_lines)) / 2)
    DOWN_SPACES = int((term_rows - (ver_lines)) / 2 + 0.5)

    if UP_SPACES < 2 or DOWN_SPACES < 3: # If can't center graphics vertically
        raise TermCantFitText(
            f"Terminal '{term_columns}x{term_rows}' can't contain "\
            f"game graphics, {ver_lines} ver. ch + 5 ch to center")

    # Start printing the graphics in the terminal
    for SPACE in range(UP_SPACES): # Print the blank spaces of above
        write(bg_color[bitd] + ''.center(term_columns) + f'{CSI}0m' + '\n')
    
    for line in GAME_INFO: write(line + '\n')

    for line in RTX_BOARD: write(line + '\n')

    if is_win or is_lose: # If end state is reached
        text = gen_bottom_text(
                term_columns, term_rows,
                lang, buttons_options,
                is_win, is_lose, bitd)

    else: text = f"{bg_color[bitd]}\n{''.center(term_columns)}" # normal state

    write(text +  '\n')
