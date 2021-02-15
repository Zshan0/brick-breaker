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
    "options_pos": [(20, 21), (20, 23), (20, 25)],
    "options": ["N E W   G A M E",
                "C O N T I N U E",
                "E X I T"],
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
    "time_pos": (170, 2)

}

GAME = {
    "dimensions": (179, 55),
    "origin": (60, 4),
    "background_color": "\u001b[40;1m",
    "brick_colors": ["\u001b[42;1m", "\u001b[43;1m", "\u001b[41m"],
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
    "dimensions": (12, 0),
    "velocity": (2, 0),
    "position": (90, 50)
}

BALL = {
    "name": "ball",
    "color": "\u001b[47m",
    "dimensions": (0, 0),
    "velocity": (3, 3),
    "position": (83, 29)
}

DELAY = 0.0001
UPDATE_BALL = 30
