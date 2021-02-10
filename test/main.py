import time
from colorama import Fore, Back, Style, init
from os import popen

init(autoreset=True)

MINY, MAXY = 1, 24
MINX, MAXX = 1, 80
FORES = [Fore.BLACK, Fore.RED, Fore.GREEN, Fore.YELLOW,
         Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
BACKS = [Back.BLACK, Back.RED, Back.GREEN, Back.YELLOW,
         Back.BLUE, Back.MAGENTA, Back.CYAN, Back.WHITE]
STYLES = [Style.DIM, Style.NORMAL, Style.BRIGHT]


class Screen:
    ''' Stores the current position of the cursor'''
    cursor_y, cursor_x = (0, 0)
    ''' Size of the screen '''
    size_x, size_y = (150, 50)

    def check_screen_size(self):
        rows, columns = popen('stty size', 'r').read().split()
        rows, columns = int(rows), int(columns)
        if (self.size_x <= columns) and (self.size_y <= rows):
            # self.user_size_x, self.user_size_y = (columns, rows)
            self.size_x, self.size_y = (columns, rows)
        else:
            print("Terminal size needs to be atleast \
                    150 x 50 (columns x rows)")

    def move_cursor(self, x, y):
        '''fills the space and gets the cursor to x, y'''

        up = self.cursor_y - y
        right = x

        if up >= 0:
            print(f"\u001b[{up}A", end='')
        else:
            print(f"\u001b[{up}B", end='')

        print(f"\u001b[{right}D", end='')

        self.update_cursor(x, y)

    def print_color_string(self, string, x, y, color):
        self.fill_screen(x, y)
        print(color + string, end='')
        self.cursor_x += (len(string) + 1)

    def update_cursor(self, x, y):
        self.cursor_y, self.cursor_x = y, x

    def fill_screen(self, x, y):
        ''' Fills screen till x, y '''

        self.update_cursor(x, y)

    def fill_rest_screen(self):
        self.fill_screen(self.size_x, self.size_y)

    def print_and_reset(self, string, x, y, color=''):
        ''' Since this is the last statement to be called for every frame
            we reset the cursor and then give a delay
        '''
        screen.print_color_string(string, x, y, color)
        # print(self.cursor_x)
        screen.fill_rest_screen()
        screen.move_cursor(0, 0)
        time.sleep(0.1)


screen = Screen()
screen.check_screen_size()


def test_string_move(string, color=''):
    length = len(string)

    for y in range(screen.size_y):
        for x in range(screen.size_x - length):
            screen.print_and_reset(string, x, y, color)


# string = "hello"
# test_string_move(string)
# screen.print_color_string(string, 0, 0, '')
# screen.fill_rest_screen()
# time.sleep(2)
# screen.move_cursor(0, 0)
# screen.print_color_string(string, 0, 1, '')


def test_fun():
    print("hello")
    # screen.move_cursor(1, 0)
    up = 1
    right = 7
    print(f"\u001b[1A", end='')
    print(f"\u001b[1000D", end='')
    print(f"\u001b[{up}B", end='')
    print(f"\u001b[{right}C", end='')

    print("test")


test_fun()
