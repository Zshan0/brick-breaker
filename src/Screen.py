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
                    150 x 50 (columns x rows)")
            _exit()

    def reset_cursor(self):
        '''cursor goes back to the starting point'''
        print('\u001b[{}A'.format(self.HEIGHT), end='')

    def print_screen(self):
        np.savetxt(sys.stdout.buffer,
                   self.screen_string,
                   fmt='%s',
                   delimiter='',
                   newline='\n')
        time.sleep(0.01)
