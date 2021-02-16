from Parameters import *
from os import popen, _exit
import numpy as np
import sys
import time


class Screen:
    ''' Size of the screen '''
    WIDTH, HEIGHT = (WIDTH, HEIGHT)

    def __init__(self):
        ''' Check the size of the terminal and initialize
            the screen array'''
        rows, columns = popen('stty size', 'r').read().split()
        rows, columns = int(rows), int(columns)

        if (self.WIDTH <= columns) and (self.HEIGHT <= rows):
            fill = BLANK + ' ' + RESET

            self.screen_string = np.zeros(
                (self.HEIGHT, self.WIDTH), dtype='<U20')
            self.screen_string.fill(fill)
        else:
            print("Terminal size needs to be atleast \
                    240 x 60 (columns x rows)")
            _exit(0)

    def reset_cursor(self):
        '''cursor goes back to the starting point'''
        print('\u001b[{}A'.format(self.HEIGHT), end='')

    def print_screen(self):
        ''' Fast print on the screen.'''
        np.savetxt(sys.stdout.buffer,
                   self.screen_string,
                   fmt='%s',
                   delimiter='',
                   newline='\n')

        time.sleep(DELAY)

    def fill_screen(self, start_pos, end_pos, color):
        ''' Given are the top left and the bottom right corner of the
            object. It is assumed that the value passed itself is
            the complete string with RESET at the end'''
        for x in range(start_pos[0], end_pos[0] + 1):
            for y in range(start_pos[1], end_pos[1] + 1):
                self.screen_string[y][x] = color
