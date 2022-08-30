import argparse
from Defaults import *

def game_parser():
    parser = argparse.ArgumentParser(
            prog="Ansi2048",
            usage="%(prog)s [options]",
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description="Unix terminal version of the game 2048")

    parser.add_argument(
            '-v','--version',
            action='version',
            version="""
%(prog)s v1.0.0
Copyright (C) 2022 Vryepa
License GPLv3+: GNU GPL version 3 or later <https://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.

Written by a human""")

    parser.add_argument(
            "-r", '--rows', 
            type=int,
            help='rows of the board',
            default=ROWS,
            metavar='')

    parser.add_argument(
            "-c", '--columns', 
            type=int,
            help='columns of the board',
            default=COLUMNS,
            metavar='')

    parser.add_argument(
            "-wt", '--wintile', 
            type=int,
            help='tile to win',
            default=WIN_TILE,
            metavar='')

    parser.add_argument(
            "-hp", '--horpad', 
            type=int,
            help='hor. padding in the tiles',
            default=HOR_PAD,
            metavar='')

    parser.add_argument(
            "-vp", '--verpad', 
            type=int,
            help='ver. padding in the tiles',
            default=VER_PAD,
            metavar='')

    parser.add_argument(
            "-trn", '--tilerowsn', 
            type=int,
            help='rows that each tile has in graphical board',
            default=TILE_ROWS_N,
            metavar='')

    parser.add_argument(
            "-tcn", '--tilecolumnsn', 
            type=int,
            help='columns that each tile has in graphical board',
            default=TILE_COLUMNS_N,
            metavar='')

    parser.add_argument(
            "-l", '--lang', 
            type=str,
            help='system language',
            default=LANG,
            choices=LANGUAGES,
            metavar='')

    parser.add_argument(
            "-bd", '--bitdepth', 
            type=int,
            help='color depth -> 1bit, 3bit, 4bit, 8bit, 24bit',
            default=BIT,
            choices=BIT_DEPTH,
            metavar='')

    args = parser.parse_args()
    return args
