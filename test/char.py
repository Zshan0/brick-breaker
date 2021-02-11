import time
from colorama import Fore, Back, Style, init
from os import popen, system
import numpy as np
import sys
import random
init(autoreset=True)

MINY, MAXY = 1, 24
MINX, MAXX = 1, 80
FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW,
         Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW,
         Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
STYLES = [Style.DIM, Style.NORMAL, Style.BRIGHT]


class Screen:
    ''' Size of the screen '''
    WIDTH, HEIGHT = (240, 60)

    def __init__(self):
        # system("clear")
        rows, columns = popen('stty size', 'r').read().split()
        rows, columns = int(rows), int(columns)
        if (self.WIDTH <= columns) and (self.HEIGHT <= rows):
            self.screen_string = np.zeros(
                (self.HEIGHT, self.WIDTH), dtype='<U20')
            self.screen_string.fill('\u001b[40m \u001b[0m')

        else:
            print("Terminal size needs to be atleast \
                    150 x 50 (columns x rows)")

    def reset_cursor(self):
        '''cursor goes back to the starting point'''
        up = self.HEIGHT
        print(f"\u001b[{up}A", end='')
        # print(f"\u001b[1000D", end='')

    def map_screen(self, val):
        characters = [(Back.CYAN + ' '), (Back.BLACK + '*')]
        return characters[val]

    def join_func(self, ar):
        return ''.join(ar)

    def print_screen(self):
        # output = np.vectorize(self.map_screen)
        np.savetxt(sys.stdout.buffer,
                   self.screen_string,
                   fmt='%s',
                   delimiter='',
                   newline='\n')
        time.sleep(0.01)


class Object:

    def __init__(self, screen, x, y):
        self.position = {"x": x, "y": y}
        self.value = ('\u001b[41mA\u001b[0m')
        screen.screen_string[y][x] = self.value

    def update_position(self, screen, x, y):
        screen.screen_string[self.position["y"]][self.position["x"]] = ' '
        screen.screen_string[y][x] = self.value
        self.position = {"x": x, "y": y}
        # print(x, y)


screen = Screen()
balls = []
for i in range(screen.HEIGHT):
    x = random.randint(0, screen.WIDTH - 1)
    balls.append(Object(screen, x, i))
ite = 0
screen.print_screen()
while True:
    for i in range(screen.HEIGHT):
        balls[i].update_position(
            screen, (balls[i].position["x"] + 1) % screen.WIDTH, i)

    screen.print_screen()
    screen.reset_cursor()
