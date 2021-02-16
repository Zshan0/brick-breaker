from Parameters import *
from Screen import Screen
from Menu import Menu
from Top import Top
from Game import Game
from Border import Border
from Player import Player
from Input import Input_class
from os import _exit


def init_game():
    ''' initializiing the objects for the game and printing the start
        screen.'''
    screen = Screen()
    menu = Menu()
    top = Top()
    border = Border()
    game = Game(screen, menu, top, border)
    player = Player(game)
    game.set_screen()
    game.set_player(player)
    # game.set_bricks()

    main_loop(game)


def main_loop(game):
    '''The main loop that won't stop running until the game is exited'''
    input_key = Input_class()
    ball_movement = 0
    while True:

        ball_movement += 1
        if ball_movement == UPDATE_BALL:
            ball_movement = 0
            game.player.move_balls()

        input_val = input_key.input_func()
        if input_val in ['a', 'd']:
            ''' Paddle has to be moved '''
            game.player.move_paddle(input_val)
        if input_val == 'q':
            _exit(0)

        game.screen.print_screen()
        game.screen.reset_cursor()


init_game()
