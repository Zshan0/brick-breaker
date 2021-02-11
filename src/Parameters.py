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
    "dimensions": (60, 60),
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
    "dimensions": (180, 4),
    "origin": (60, 0),
    "background_color": '\u001b[40;1m',
    "text_color": '\u001b[40m\u001b[31;1m',
    "heart_icon": 'LIVES',
    "heart_pos": (61, 2),
    "heart_color": '\u001b[31;1m',
    "time_icon": 'TIME',
    "time_color": '\u001b[37;1m',
    "time_pos": (180, 2)

}

GAME = {
    "width": 180,
    "height": 56,
    "x": 60,
    "y": 4
}
