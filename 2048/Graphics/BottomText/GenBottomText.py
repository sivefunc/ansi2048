from wcwidth import wcswidth as len # RM it if dont want translated center text

from Graphics.GameColors import simple_text_color, focus_text_color, bg_color
from Graphics.Exceptions.TermCantFitTXT import TermCantFitText
from Graphics.BottomText.LoseMSG import LOSE
from Graphics.BottomText.WinMSG import WIN
from Graphics.BottomText.NGMSG import NEW_GAME
from Graphics.BottomText.KGMSG import KEEP_GOING
from Graphics.BottomText.ExitMSG import EXIT
from Graphics.CenterText import center_text

def gen_bottom_text(
        column_count, row_count,
        lang, buttons_options,
        is_win, is_lose, bit_depth):
    
    """
    Generate the bottom text when the end state of board is reached
    """

    if is_win and is_lose:
        YOU_DID, OPTION1, OPTION2 = WIN[lang], NEW_GAME[lang], EXIT[lang]

    elif is_win:
        YOU_DID, OPTION1, OPTION2 = WIN[lang], KEEP_GOING[lang], EXIT[lang]
    
    else:
        YOU_DID, OPTION1, OPTION2 = LOSE[lang], NEW_GAME[lang], EXIT[lang]
    
    text_len = len(f'{YOU_DID}, <{OPTION1}> - <{OPTION2}>')
    free_spaces = column_count - text_len
    if free_spaces < 6: # If the bottom text can't be centered
        raise TermCantFitText(
            f"Terminal '{column_count}x{row_count}' can't contain "\
            f"game bottom text, {text_len} hor. ch + 6 ch to center")
    
    if buttons_options[-1]:
        message = f"{simple_text_color[bit_depth]}{YOU_DID}, "\
                f"<{OPTION1.upper()}> - {focus_text_color[bit_depth]}"\
                f"<{OPTION2.upper()}>"
                
    elif buttons_options[0]:
        message = f"{simple_text_color[bit_depth]}{YOU_DID}, "\
                f"{focus_text_color[bit_depth]}<{OPTION1.upper()}>"\
                f"{simple_text_color[bit_depth]} - <{OPTION2.upper()}>"

    return f"{bg_color[bit_depth]}\n{center_text(message, free_spaces)}"
