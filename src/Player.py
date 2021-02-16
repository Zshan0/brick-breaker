from Parameters import *
from Paddle import Paddle
from Ball import Ball
import time


class Player:
    def __init__(self, game):
        self.game = game
        ball = Ball(game)
        self.paddle = Paddle(game, ball)
        self.lives = -1
        self.init_time = -1
        self.option = 0
        self.powers = []
        self.balls = [ball]
        self.score = 0
        self.status = 0

    def reduce_life(self):
        self.lives = self.lives - 1
        if self.lives == 0:
            return False
        else:
            return True

    def time_init(self):
        self.init_time = time.time()

    def move_paddle(self, input):
        if input == 'a':
            value = -1
        elif input == 'd':
            value = 1

        self.paddle.move_paddle(self.game, value)

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

    def game_start(self):
        ''' Destroy the original Player object and create a new one'''
        self.status = 1
