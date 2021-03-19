from Parameters import *
import time
import random
from os import _exit, system
from Body import Body
from Bomb import Bomb
class Boss:
    def __init__(self, game):
        self.game = game
        self.body = Body(game)
        self.lives = MAX_LIVES
        self.bombs = []
        self.status = 0
        self.game.set_boss_bar(self.lives)
        self.bomb_time = time.time()

    def bomb_check(self):
        time_passed = time.time() - self.bomb_time
        if time_passed >= BOMB_SPAN:
            self.bomb_time = time.time()
            self.bomb_increase()

    def reduce_life(self):
        self.lives = self.lives - 1
        self.game.set_boss_bar(self.lives)
        if self.lives in BRICK_LIFE:
            region = [
                self.game.brick_region[0] + 2,
                self.game.brick_region[0] + 3
            ]
            self.game.delete_bricks()
            self.game.set_bricks(region, True)

    def move_boss(self, input):
        if input == " ":
            value = 0
        elif input == "a":
            value = -1
        elif input == "d":
            value = 1

        self.body.move_body(self.game, value)

    def move_bombs(self):

        for bomb in self.bombs:
            if bomb.move_bomb(self.game):
                continue
            """ If move_ball() returns False it means the ball has to be
                deleted"""
            self.bombs.remove(bomb)
            bomb.delete(self.game)

        self.bomb_check()

    def bomb_increase(self):
        """ Dropping a bomb"""

        bomb = Bomb(self.game)
        new_pos = [self.body.position[0] + random.randint(0, self.body.dimensions[0]),
                   self.body.position[1]]
        bomb.displace(self.game, new_pos)
        self.body.displace(self.game, self.body.position)
        self.bombs.append(bomb)
