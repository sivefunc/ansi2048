from Graphics.Exceptions.TermCantFitTXT import TermCantFitText
from Graphics.GameColors import tile_colors, bg_color, pad_color
from Graphics.CenterText import center_text

ESC = chr(27)
CSI = ESC + '['

def gen_game_board(
            board, column_count, row_count,
            tile_rows_n, tile_columns_n, hor_pad,
            ver_pad, bit_depth):

    new_board = []

    # Non free spaces that each row of the board has
    len_bar = (
            tile_columns_n * len(board[0])
            + len(board[0]) * hor_pad + hor_pad)
    
    if (free_spaces := column_count -  len_bar) < 6: # If row can't be centered
        raise TermCantFitText(
            f"Terminal '{column_count}x{row_count}' can't contain "\
            f"game board, {len_bar} hor. ch + 6 ch to center")
    
    # Horizontal bar
    hor_bar = center_text(f"{pad_color[bit_depth]}{' ' * len_bar}{CSI}0m",
                                                                free_spaces)

    hor_bar_w_bg = bg_color[bit_depth] + f'm{bg_color[bit_depth]}'.join(
                                                        hor_bar.rsplit('m', 1))
    
    for pad in range(ver_pad): new_board.append(hor_bar_w_bg)
    
    # Generating rectangular board
    for tiles in board:
        rows = ["" for i in range(tile_rows_n)]
        for tile in tiles:
            if tile in tile_colors: color = tile_colors[tile][bit_depth]
            else: color = tile_colors[-1][bit_depth]
            
            for idx, row in enumerate(rows):
                # Place tile number in the row of center
                if idx == int(len(rows) / 2 + 0.5) - 1:
                    rows[idx] += f"{pad_color[bit_depth]}{hor_pad * ' '}"\
                            f"{color}{str(tile).center(tile_columns_n)}{CSI}0m"
                
                else: # Place tile margin in the given row idx
                    rows[idx] += f"{pad_color[bit_depth]}{hor_pad * ' '}"\
                            f"{color}{' ' * tile_columns_n}{CSI}0m"

        for row in rows:
            # Add horizontal padding in the right side of row
            row = f"{pad_color[bit_depth]}{hor_pad * ' '}{CSI}0m".join(
                                                    row.rsplit(f'{CSI}0m', 1))

            centered_row = center_text(row, free_spaces)
            text_w_bg = bg_color[bit_depth] + f'm{bg_color[bit_depth]}'.join(
                                                centered_row.rsplit('m', 1))
            new_board.append(text_w_bg)
        
        for pad in range(ver_pad): new_board.append(hor_bar_w_bg)
        rows.clear()
    
    return new_board
