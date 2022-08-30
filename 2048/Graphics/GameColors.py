# Game colors depth
# |0| 1bit - |1| 3 bit - |2| 4 bit - |3| 8bit - |4| 24bit 
# https://en.wikipedia.org/wiki/Color_depth
#
# Initial Colors got from 2048 "Original" Author:
# https://github.com/gabrielecirulli/2048/blob/master/style/main.scss
# https://github.com/gabrielecirulli/2048/blob/master/style/main.css
#
# Also got some colors using grabc in this Qt Implementation of 2048
# https://salsa.debian.org/alejandro/2048-qt

ESC = chr(27)
CSI = ESC + '['

tile0 = [
        f'{CSI}37;47m', # 1bit
        f'{CSI}37;47m', # 3bit
        f'{CSI}90;100m', # 4bit
        f'{CSI}1;38;5;180;48;5;180m', # 8bit
        f'{CSI}1;38;2;205;193;180;48;2;205;193;180m'] #24bit

tile2 = [
        f'{CSI}30;47m',
        f'{CSI}30;46m',
        f'{CSI}30;106m',
        f'{CSI}1;38;5;236;48;5;222m',
        f'{CSI}1;38;2;119;110;101;48;2;238;228;218m']

tile4 = [
        f'{CSI}30;47m',
        f'{CSI}30;46m',
        f'{CSI}30;46m',
        f'{CSI}1;38;5;236;48;5;223m',
        f'{CSI}1;38;2;119;110;101;48;2;237;224;200m']

tile8 = [
        f'{CSI}30;47m',
        f'{CSI}30;41m',
        f'{CSI}37;101m',
        f'{CSI}1;38;5;231;48;5;216m',
        f'{CSI}1;38;2;249;246;242;48;2;242;177;121m']

tile16 = [
        f'{CSI}30;47m',
        f'{CSI}30;41m',
        f'{CSI}37;101m',
        f'{CSI}1;38;5;231;48;5;210m',
        f'{CSI}1;38;2;249;246;242;48;2;245;149;99m']

tile32 = [
        f'{CSI}30;47m',
        f'{CSI}30;41m',
        f'{CSI}37;101m',
        f'{CSI}1;38;5;231;48;5;204m',
        f'{CSI}1;38;2;249;246;242;48;2;246;124;95m']

tile64 = [
        f'{CSI}30;47m',
        f'{CSI}30;41m',
        f'{CSI}37;41m',
        f'{CSI}1;38;5;231;48;5;197m',
        f'{CSI}1;38;2;249;246;242;48;2;246;94;59m']

tile128 = [
        f'{CSI}30;47m',
        f'{CSI}30;43m',
        f'{CSI}30;103m',
        f'{CSI}1;38;5;236;48;5;228m',
        f'{CSI}1;38;2;249;246;242;48;2;237;207;114m']

tile256 = [
        f'{CSI}30;47m',
        f'{CSI}30;43m',
        f'{CSI}30;103m',
        f'{CSI}1;38;5;236;48;5;227m',
        f'{CSI}1;38;2;249;246;242;48;2;237;204;97m']

tile512 = [
        f'{CSI}30;47m',
        f'{CSI}30;43m',
        f'{CSI}30;103m',
        f'{CSI}1;38;5;236;48;5;226m',
        f'{CSI}1;38;2;249;246;242;48;2;237;200;80m']

tile1024 = [
        f'{CSI}30;47m',
        f'{CSI}30;43m',
        f'{CSI}30;103m',
        f'{CSI}1;38;5;236;48;5;221m',
        f'{CSI}1;38;2;249;246;242;48;2;237;197;63m']

tile2048 = [
        f'{CSI}30;47m',
        f'{CSI}30;43m',
        f'{CSI}30;43m',
        f'{CSI}1;38;5;236;48;5;220m',
        f'{CSI}1;38;2;249;246;242;48;2;237;194;46m']

unknown_tile = [
        f'{CSI}30;47m',
        f'{CSI}30;45m',
        f'{CSI}37;105m',
        f'{CSI}1;38;5;231;48;5;236m',
        f'{CSI}1;38;2;249;246;242;48;2;60;58;50m']    

tile_colors = {
        -1: unknown_tile, 0: tile0, 2: tile2, 4: tile4, 8: tile8, 16: tile16,
        32: tile32, 64: tile64, 128: tile128, 256: tile256, 512: tile512,
        1024: tile1024, 2048: tile2048}

score_letter_color = [
        f'{CSI}37;40m',
        f'{CSI}37;40m',
        f'{CSI}37;40m',
        f'{CSI}1;38;5;220;48;5;138m',
        f'{CSI}1;38;2;237;227;213;48;2;187;173;160m']

score_number_color = [
        f'{CSI}37;40m',
        f'{CSI}31;40m',
        f'{CSI}91;40m',
        f'{CSI}1;38;5;7;48;5;138m',
        f'{CSI}1;38;2;249;246;242;48;2;187;173;160m']

simple_text_color = [
        f'{CSI}30;47m',
        f'{CSI}30;47m',
        f'{CSI}90;47m',
        f'{CSI}1;38;5;173;48;5;7m',
        f'{CSI}1;38;2;187;173;160;48;2;250;249;239m']

focus_text_color = [
        f'{CSI}30;47m',
        f'{CSI}31;47m',
        f'{CSI}91;47m',
        f'{CSI}1;38;5;236;48;5;7m',
        f'{CSI}1;38;2;119;110;101;48;2;250;249;239m']

bg_color = [
        f'{CSI}47m',
        f'{CSI}47m',
        f'{CSI}47m',
        f'{CSI}48;5;7m',
        f'{CSI}48;2;250;248;239m']

pad_color = [
        f'{CSI}40m',
        f'{CSI}40m',
        f'{CSI}40m',
        f'{CSI}48;5;137m',
        f'{CSI}48;2;187;173;160m']
