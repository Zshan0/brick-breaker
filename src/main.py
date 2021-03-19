from Parameters import *
from Screen import Screen
from Menu import Menu
from Top import Top
from Game import Game
from Border import Border
from Player import Player
from Input import Input_class
import os


# details = {"score": 0, "lives": 0}

def init_game(player_status, level, details={"score": 0, "lives": MAX_LIVES}):
    """initializiing the objects for the game and printing the start
    screen."""
    os.system("stty -echo")
    screen = Screen()
    menu = Menu()
    top = Top()
    border = Border()
    game = Game(screen, menu, top, border, level)
    game.set_screen()
    player = Player(game)
    game.set_player(player)

    game.player.score = details["score"]
    game.player.lives = details["lives"]
    game.set_lives(details["lives"])
    game.set_level()
    game.top.set_score(game.screen, details["score"])


    if player_status == 1:
        player.game_start()
        if level == 3:
            """Boss level-> No bricks"""
            game.set_boss()
        elif level > 3:
            game.game_over()
        else:
            pass
            game.set_bricks()

    main_loop(game)


def main_loop(game):
    """The main loop that won't stop running until the game is exited"""
    input_key = Input_class()
    ball_movement = 0
    while True:
        game.screen.print_screen()
        game.screen.reset_cursor()

        if game.player.status == 0:
            """ The game has not started yet"""
            input_val = input_key.input_func()

            if game.player.input_option(input_val):
                continue
            else:
                """ The game was paused and hence needs to be reset"""
                init_game(1, game.level)

        game.player.time_update()
        ball_movement += 1
        if ball_movement == REFRESH_RATE:
            game.reset_screen()
            ball_movement = 0

        game.player.move_balls()
        game.player.move_powerups()
        if game.level == 3:
            game.boss_check()
            ''' Moving bombs and spawning more if the time has passed'''
            game.boss.move_bombs()
        else:
            if game.bricks_check():
                init_game(1, game.level + 1, {
                    "score": game.player.score,
                    "lives": game.player.lives
                    })

        input_val = input_key.input_func()
        if input_val in ["a", "d", " "]:
            """ Paddle has to be moved """
            game.player.move_paddle(input_val)
            if game.level == 3:
                """ Existing boss also has to be moved"""
                game.boss.move_boss(input_val)
        elif input_val == "q":
            game.player.game_pause()
        elif input_val == "n":
            if game.level == 3:
                game.player.game_over()
            else:
                init_game(1, game.level + 1, {
                    "score": game.player.score,
                    "lives": game.player.lives
                    })


init_game(0, 1)
