from colorama import Fore, Back, Style, init
init(autoreset=True)


# COLORS
COLORS = {
    "cyan": Back.CYAN,
    "black": Back.BLACK,
}

# Object
OBJECTS = {
    "background": ' ',
    "paddle": 1,
}

BLANK = '\u001b[37;1m'
RESET = '\u001b[0m'

''' SCREEN DIMENSIONS AND DIMENSIONS:
        the colors are the starting values, after which the displayed
        value is to be displayed and then RESET is to be applied.

'''
WIDTH, HEIGHT = (240, 60)
MENU = {
    "dimensions": (59, 59),
    "origin": (0, 0),
    "background_color": '\u001b[40;1m',
    "text_color": '\u001b[40m\u001b[37;1m',
    "options_color": '\u001b[40m\u001b[33;1m',
    "selected_option_color": '\u001b[40m\u001b[32;1m',
    "name_pos": (15, 10),
    "name": "B R I C K - B R E A K E R",
    "options_pos": [(20, 21), (20, 23), (20, 25), (20, 27), (20, 29), (20, 31)],
    "options": ["1. N E W   G A M E",
                "2. C O N T I N U E",
                "3. E X I T",
                "INSTRUCTIONS:",
                "Press q to pause",
                "After Pausing press the option number."],
}

TOP = {
    "dimensions": (179, 4),
    "origin": (60, 0),
    "background_color": '\u001b[40;1m',
    "text_color": '\u001b[40m\u001b[31;1m',
    "heart_icon": 'LIVES',
    "heart_pos": (1, 2),
    "heart_color": '\u001b[31;1m',
    "time_icon": 'TIME',
    "time_color": '\u001b[37;1m',
    "time_pos": (170, 2),
    "game_over_pos": (50, 2),
    "game_over_text": "G A M E-O V E R",
    "score_pos": (80, 2),
    "score_icon": "SCORE",
    "bar_pos": (100, 2),
    "level_pos": (20, 2),
    "level_icon": "level"
}

GAME = {
    "dimensions": (179, 55),
    "origin": (60, 4),
    "background_color": "\u001b[40;1m",
    "brick_colors": ["\u001b[42;1m", "\u001b[43;1m", "\u001b[41m",
                     "\u001b[47m", "\u001b[45;1m"],
    "brick_region": (0, 10),
    "max_bricks": 100,
    "max_explosive": 8,
}


''' Consists of list of pair of coordinates which decide from what point
    to what point the border is supposed to stretch. The border only
    exists outside the game. The border on the bottom and the right side
    of the screen will be done by placing the objects as barriers.'''
BORDER = {
    "dimensions": [
        [(0, 0), (0, 59)],
        [(0, 0), (239, 0)],
        [(59, 0), (59, 59)],
        [(59, 3), (239, 3)],
        [(239, 0), (239, 5)],
        [(0, 59), (59, 59)]],
    "color": "\u001b[47m"
}

''' Objects: contains the dictionary that defines the object
    contains: color, width, height, velocity'''

PADDLE = {
    "name": "paddle",
    "color": "\u001b[47m",
    "dimensions": (10, 0),
    # "dimensions": (179, 0),
    "velocity": (1, 0),
    # "position": (83, 15),
    "position": (83, 30),
    "change": 2
}

BALL = {
    "name": "ball",
    # "color": "\u001b[47m",
    "color": "\u001b[40;1m",
    "character": "O",
    "dimensions": (0, 0),
    "velocity": (0.5, 0.5),
    "position": (83, 29)
    # "position": (83, 14)
}

LASER = {
    "name": "laser",
    # "color": "\u001b[47m",
    "color": "\u001b[43;1m",
    "character": "O",
    "dimensions": (0, 0),
    "velocity": (0, -1)
}


BRICK = {
    "name": "brick",
    "dimensions": (10, 1),
    "velocity": (0, 0)
}

POWERUP = {
    "name": "powerup",
    "color": "\u001b[40m\u001b[32;1m",
    "text": ["E", "S", "B", "F", "T", "P", "L"],
    # "text": ["L"],
    "dimensions": (0, 0),
    "velocity": (0, 0.3),
}

BODY = {
    "name": "body",
    "color": "\u001b[42;1m",
    "dimensions": (50, 0),
    # "dimensions": (179, 0),
    "velocity": (1, 0),
    # "position": (0, 30)
    "position": (83, 0),
    "change": 2
}

BOMB = {
    "name": "bomb",
    # "color": "\u001b[47m",
    "color": "\u001b[40;1m",
    "character": "B",
    "dimensions": (0, 0),
    "velocity": (0, 0.5),
    "position": (83, 6)
}

DELAY = 0
TIMEOUT = 0.1
UPDATE_BALL = 1
MAX_LIVES = 4

POWERUP_SPAN = 10
POWERUP_SPAN = 5
BRICK_SCORE = [10, 20, 40, 0, 800]
BOMB_SPAN = 1
BRICK_LIFE = [3, 1]
BRICK_SHIFT = 20
LASER_TIME = 15
LASER_SPAN = 1
LASER_COLOR = "\u001b[43;1m"
GRAVITY = 0.1
REFRESH_RATE = 10
