import time
from Screen import Screen
from Menu import Menu
from Top import Top

screen = Screen()
menu = Menu()
top = Top()
screen.print_screen()
time.sleep(1)
screen.reset_cursor()
menu.set_screen(screen)
top.set_screen(screen)
screen.print_screen()
screen.reset_cursor()
time.sleep(10)
