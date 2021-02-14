from Parameters import *
import time
from Screen import Screen
from Menu import Menu
from Top import Top
from Game import Game
from Border import Border
from Object import Object


def init_game():
    ''' initializiing the objects for the game and printing the start
        screen.'''
    screen = Screen()
    menu = Menu()
    top = Top()
    border = Border()
    game = Game(screen, menu, top, border)
    game.set_screen()

    paddle = Object(game, PADDLE, PADDLE["position"])

    main_loop(game, paddle)


def main_loop(game, paddle):
    '''The main loop that won't stop running until the game is exited'''
    while True:
        game.screen.print_screen()
        game.screen.reset_cursor()

        old_pos = paddle.position
        new_pos = [(old_pos[0] + 1) %
                   (game.dimensions[0] - (paddle.dimensions[0])),
                   old_pos[1]]

        paddle.displace(game, new_pos)


init_game()
