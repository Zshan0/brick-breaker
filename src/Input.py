import sys
import termios
import tty
import signal
import time
from Parameters import *


class Input_class:
    ''' Taking input from the terminal'''

    def timeout_handler(self, signum, frame):
        raise TimeoutError

    def input_char(self):
        '''def to call function'''
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            value = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return value

    def input_func(self, timeout=0.1):

        signal.signal(signal.SIGALRM, self.timeout_handler)
        signal.setitimer(signal.ITIMER_REAL, timeout)

        try:
            value = self.input_char()
            signal.alarm(0)

            if value in [b'a', b'd', b'\r', b' ', b'q']:
                time.sleep(timeout)

            return value
        except:
            signal.signal(signal.SIGALRM, signal.SIG_IGN)
            return None
