from Parameters import *
from Paddle import Paddle
from Ball import Ball
import time
from os import _exit, system


class Player:
    def __init__(self, game):
        self.game = game
        ball = Ball(game, 1)
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
        self.powerups = []

    def reduce_life(self):

        self.lives = self.lives - 1
        self.game.set_lives(self.lives)

    def time_update(self):
        time_diff = time.time() - self.init_time
        self.game.top.set_time(self.game.screen, time_diff)

    def time_init(self):
        self.init_time = time.time()

    def move_paddle(self, input):
        if input == " ":
            self.paddle.release_ball()
            return
        elif input == "a":
            value = -1
        elif input == "d":
            value = 1

        self.paddle.move_paddle(self.game, value)

    def game_reset(self):
        ball = Ball(self.game)
        self.paddle.delete(self.game)
        self.paddle = Paddle(self.game, ball)
        self.balls = [ball]
        self.powerups = []

    def game_over(self):
        self.game_pause()
        self.game.game_over()

    def move_balls(self):

        for ball in self.balls:
            if ball.is_held:
                continue
            if ball.move_ball(self.game):
                continue
            """ If move_ball() returns False it means the ball has to be
                deleted"""
            ball.delete(self.game)
            self.balls.remove(ball)

        if len(self.balls) == 0:
            """ All the balls are gone"""
            self.reduce_life()
            if self.lives > 0:
                self.game_reset()
            else:
                """ All the lives are gone"""
                self.game_over()

    def move_powerups(self):
        for powerup in self.powerups:
            if not powerup.move_powerup(self.game):
                self.powerups.remove(powerup)

        self.powerup_check()

    def ball_increase(self):
        """ Doubling the balls with opposite x velocity"""

        new_balls = []

        for ball in self.balls:
            new_ball = Ball(self.game)
            new_ball.velocity = [-ball.velocity[1], ball.velocity[0]]
            new_ball.displace(self.game, ball.position)
            new_balls.append(new_ball)

        self.balls.extend(new_balls)

    def ball_fast(self):
        for ball in self.balls:
            ball.velocity = [2 * a for a in ball.velocity]

    def laser_shot(self):
        self.laser_time = time.time()
        laser = Ball(self.game, 2)
        self.balls.append(laser)

    def laser_mode(self, mode):
        ''' Changing the color of paddle'''
        if mode:
            self.laser_time = time.time()
            self.paddle.color = LASER_COLOR
            self.paddle.displace(self.game, self.paddle.position)
            self.laser_shot()
        else:
            self.paddle.color = PADDLE["color"]
            self.paddle.displace(self.game, self.paddle.position)

    def powerup_gain(self, powerup):
        is_there = list(
            filter(
                lambda power: power["powerup"].character == powerup.character,
                self.powers,
            )
        )
        if len(is_there) > 0:
            """ Powerup already present"""
            self.powers.remove(is_there[0])
            self.powers.append({"powerup": powerup, "time": time.time()})
            return

        self.powers.append({"powerup": powerup, "time": time.time()})

        if powerup.character == "E":
            """ Expand the paddle"""
            self.paddle.expand_paddle(self)
        elif powerup.character == "S":
            """ Shrink the paddle"""
            self.paddle.shrink_paddle(self)
        elif powerup.character == "B":
            """ Ball multiplier"""
            self.ball_increase()
        elif powerup.character == "L":
            """ Laser Shooting"""
            self.laser_mode(True)

    def powerup_loss(self, powerup_dict):
        powerup = powerup_dict["powerup"]

        if powerup.character == "E":
            """ Expand the paddle"""
            self.paddle.shrink_paddle(self)
        elif powerup.character == "S":
            """ Shrink the paddle"""
            self.paddle.expand_paddle(self)
        elif powerup.character == "L":
            self.laser_mode(False)

        self.powers.remove(powerup_dict)

    def powerup_check(self):
        """ Checks if the powerup span has runout"""
        for power in self.powers:
            time_passed = time.time() - power["time"]
            if power["powerup"].character == "L":
                last_shot = time.time() - self.laser_time
                if last_shot >= LASER_SPAN:
                    self.laser_shot()

                if time_passed >= LASER_TIME:
                    self.powerup_loss(power)

            if time_passed >= POWERUP_SPAN:
                self.powerup_loss(power)

    def game_start(self):
        """ Destroy the original Player object and create a new one"""
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
            system("stty echo")
            _exit(0)
        else:
            return True

    def score_reset(self):
        self.score = 0

    def score_increase(self, strength):
        self.score += BRICK_SCORE[strength]
        self.game.top.set_score(self.game.screen, self.score)
