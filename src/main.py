from Parameters import *
from Screen import Screen
from Menu import Menu
from Top import Top
from Game import Game
from Border import Border
from Player import Player
from Input import Input_class
from os import _exit


def init_game(player_status):
    ''' initializiing the objects for the game and printing the start
        screen.'''
    screen = Screen()
    menu = Menu()
    top = Top()
    border = Border()
    game = Game(screen, menu, top, border)
    game.set_screen()
    player = Player(game)
    game.set_player(player)

    if player_status == 1:
        player.game_start()
        game.set_bricks()

    main_loop(game)


def main_loop(game):
    '''The main loop that won't stop running until the game is exited'''
    input_key = Input_class()
    ball_movement = 0
    while True:
        game.screen.print_screen()
        game.screen.reset_cursor()

        if game.player.status == 0:
            ''' The game has not started yet'''
            input_val = input_key.input_func()

            if game.player.input_option(input_val):
                continue
            else:
                ''' The game was paused and hence needs to be reset'''
                init_game(1)

        game.player.time_update()
        ball_movement += 1
        if ball_movement == UPDATE_BALL:
            ball_movement = 0
            game.player.move_balls()

        input_val = input_key.input_func()
        if input_val in ['a', 'd', ' ']:
            ''' Paddle has to be moved '''
            game.player.move_paddle(input_val)
        elif input_val == 'q':
            game.player.game_pause()


init_game(0)
