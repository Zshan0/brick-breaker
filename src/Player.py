from Parameters import *
from Paddle import Paddle
from Ball import Ball
import time
from os import _exit


class Player:
    def __init__(self, game):
        self.game = game
        ball = Ball(game)
        self.paddle = Paddle(game, ball)
        self.lives = 3
        self.init_time = -1
        self.option = 0
        self.powers = []
        self.balls = [ball]
        self.score = 0
        self.status = 0
        self.init_time = time.time()
        self.game.set_lives(self.lives)

    def reduce_life(self):

        self.lives = self.lives - 1
        self.game.set_lives(self.lives)
        if self.lives == 0:
            return False
        else:
            return True

    def time_update(self):
        time_diff = time.time() - self.init_time
        self.game.top.set_time(self.game.screen, time_diff)

    def time_init(self):
        self.init_time = time.time()

    def move_paddle(self, input):
        if input == ' ':
            self.paddle.release_ball()
            return
        elif input == 'a':
            value = -1
        elif input == 'd':
            value = 1

        self.paddle.move_paddle(self.game, value)

    def game_reset(self):
        ball = Ball(self.game)
        self.paddle.delete(self.game)
        self.paddle = Paddle(self.game, ball)
        self.balls = [ball]

    def game_over(self):
        self.game_pause()
        self.game.game_over()

    def move_balls(self):

        for ball in self.balls:
            if ball.is_held:
                continue
            if ball.move_ball(self.game):
                continue
            ''' If move_ball() returns False it means the ball has to be
                deleted'''
            ball.delete(self.game)
            self.balls.remove(ball)

        if len(self.balls) == 0:
            ''' All the balls are gone'''
            if self.reduce_life():
                self.game_reset()
            else:
                ''' All the lives are gone'''
                self.game_over()

    def game_start(self):
        ''' Destroy the original Player object and create a new one'''
        self.status = 1

    def game_pause(self):
        self.status = 0

    def input_option(self, option):
        if option == "1":
            self.time_init()
            self.game_start()
            return False
        elif option == "2":
            self.game_start()
            return True
        elif option == "3":
            _exit(0)
        else:
            return True
