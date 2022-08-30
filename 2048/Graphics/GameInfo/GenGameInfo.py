from wcwidth import wcswidth as len
from Graphics.Exceptions.TermCantFitTXT import TermCantFitText
from Graphics.GameInfo.ScoreMSG import SCORE
from Graphics.GameInfo.BestMSG import BEST
from Graphics.GameInfo.DescMSG import DESCRIPTION
from Graphics.CenterText import center_text
from Graphics.GameColors import (
        score_letter_color, score_number_color,
        simple_text_color, focus_text_color,
        bg_color, pad_color)

def gen_game_info(
        column_count, row_count, lang, 
        score, score_added, best, bit_depth):
    
    # 2048 game infe <Name of Game> <New score> <Best Score> and <Description>

    # 1 - row ' _   _          __   OOOO+12OOOO OOOOOOOOOOO'.center()
    # 2 - row '/ ) / \  |  |  (__)  OOOSCOREOOO OOOOBESTOOO'.center()
    # 3 - row ' / |   | |__|_ /  \  OOOOO20OOOO OOOOO20OOOO'.center()
    # 4 - row '/__ \_/     |  \__/  OOOOOOOOOOO OOOOOOOOOOO'.center()
    # 5 - row '                                            '.center()
    # 6 - row ' Join the numbers and get to the 2048 Tile! '.center()
    # 7 - row '                                            '.center()

    logo_text1 =    ' _   _          __   '
    logo_text2 =    '/ ) / \  |  |  (__)  '
    logo_text3 =    ' / |   | |__|_ /  \  '
    logo_text4 =    '/__ \_/     |  \__/  '
    logo_len = len(logo_text1)
    
    f_sq = len(SCORE[lang])+4 if len(SCORE[lang])>len(score) else len(score)+ 4
    s_sq = len(BEST[lang]) + 4 if len(BEST[lang]) > len(best) else len(best)+ 4

    game_info_len = logo_len + f_sq + 1 + s_sq
    gi_free_spaces = column_count - game_info_len
    
    description_text = DESCRIPTION[lang]
    gd_free_spaces = column_count - len(description_text)

    if gi_free_spaces < 6: # If game info can't be centered
        raise TermCantFitText(
            f"Terminal '{column_count}x{row_count}' can't contain "\
            f"game info, {game_info_len} hor. ch + 6 ch to center")
    
    elif gd_free_spaces < 6: # If the desc 'Join the ...' can't be centered
        raise TermCantFitText(
            f"Terminal '{column_count}x{row_count}' can't contain "\
            f"game desc. {len(description_text)} hor. ch + 6 ch to center")
    
    GAME_INFO = [

            # 1 - row ' _   _          __   OOOO+12OOOO OOOOOOOOOOO'.center()
bg_color[bit_depth] + center_text(f"{focus_text_color[bit_depth]}{logo_text1}"\
                    f"{pad_color[bit_depth]}{score_added.center(f_sq)}"\
                    f"{bg_color[bit_depth]} {pad_color[bit_depth]}"\
                    f"{' ' * s_sq}{bg_color[bit_depth]}", gi_free_spaces),

            # 2 - row '/ ) / \  |  |  (__)  OOOSCOREOOO OOOOBESTOOO'.center()
bg_color[bit_depth] + center_text(f"{focus_text_color[bit_depth]}{logo_text2}"\
                    f"{score_letter_color[bit_depth]}"\
                    f"{center_text(SCORE[lang], f_sq - len(SCORE[lang]))}"\
                    f"{bg_color[bit_depth]} {score_letter_color[bit_depth]}"\
                    f"{center_text(BEST[lang], s_sq - len(BEST[lang]))}"\
                    f"{bg_color[bit_depth]}", gi_free_spaces),
            
            # 3 - row ' / |   | |__|_ /  \  OOOOO20OOOO OOOOO20OOOO'.center()
bg_color[bit_depth] + center_text(f"{focus_text_color[bit_depth]}{logo_text3}"\
                    f"{score_number_color[bit_depth]}{score.center(f_sq)}"\
                    f"{bg_color[bit_depth]} {score_number_color[bit_depth]}"\
                    f"{best.center(s_sq)}{bg_color[bit_depth]}",
                    gi_free_spaces),
            
            # 4 - row '/__ \_/     |  \__/  OOOOOOOOOOO OOOOOOOOOOO'.center()
bg_color[bit_depth] + center_text(f"{focus_text_color[bit_depth]}{logo_text4}"\
                f"{pad_color[bit_depth]}{' ' * f_sq}{bg_color[bit_depth]} "\
                f"{pad_color[bit_depth]}{' ' * s_sq}{bg_color[bit_depth]}",
                gi_free_spaces),

            # 5 - row '                                            '.center()
bg_color[bit_depth] + ' ' * column_count,

            # 6 - row 'Join the numbers and get to the 2048 Tile!'.center()
simple_text_color[bit_depth] + f'{focus_text_color[bit_depth]}2048'.join(
                center_text(description_text, gd_free_spaces).split('2048')),
            # DESC txt wont have focus text if '2048' isn't in given desc lang
            # e.g -> latin

            # 7 - row '                                            '.center()
bg_color[bit_depth] + ' ' * column_count,
    ]
    
    return GAME_INFO
