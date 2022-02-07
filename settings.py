from parse_level import LevelParser


from parse_level import LevelParser

level_map = [
    "                            ",
    "                            ",
    "                            ",
    " XX    XXX            XX    ",
    " XX P                       ",
    " XXXX         XX         XX ",
    " XXXX       XX              ",
    " XX    X  XXXX    XX  XX    ",
    "       X  XXXX    XX  XXX   ",
    "    XXXX  XXXXXX  XX  XXXX  ",
    "XXXXXXXX  XXXXXX  XX  XXXX  ",
]

level_map = LevelParser(600, 600)

tile_size = 60
screen_width = 600
screen_height = 600
