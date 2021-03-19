from Parameters import *
from Object import Object
from PowerUp import PowerUp
from random import randint


class Brick(Object):
    def __init__(self, game, strength, position):
        desc = BRICK
        desc.update({"color": game.brick_colors[strength]})
        super(Brick, self).__init__(game, desc, position)
        self.strength = strength
        self.game = game
        self.color = game.brick_colors[strength]
        self.is_blinking = randint(0, 1) == 1

        no_powerups = len(POWERUP["text"])
        powerup_num = randint(0, no_powerups - 1)
        powerup_pos = [int(self.position[0] + (self.dimensions[0] / 2)),
                       int(self.position[1] + (self.dimensions[1]))]

        self.powerup = PowerUp(powerup_num, powerup_pos)

    def blink(self):
        if not self.is_blinking:
            return

        self.strength = ((self.strength + 1) %
                        (len(self.game.brick_colors) - 2))

        self.color = self.game.brick_colors[self.strength]
        self.displace(self.game, self.position)

    def collision_reaction(self, breakable, ball=None):
        if breakable == "OP":
            if self.strength == len(self.game.brick_colors) - 1:
                self.strength = -1
                self.game.explosive_brick(self)

                ''' Destroying all the explosive bricks'''
                for brick in self.game.bricks:
                    if brick.strength == len(self.game.brick_colors) - 1:
                        brick.strength = -1
                        self.game.explosive_brick(brick)
                        brick.delete(self.game)
                        if brick in self.game.bricks:
                            self.game.bricks.remove(brick)

            if self.powerup is not None:
                self.powerup.release_powerup(self.game, self, ball)
                self.delete(self.game)

            return False

        if self.strength == len(self.game.brick_colors) - 2:
            ''' Unbreakable ones'''
            return True

        if self.strength == len(self.game.brick_colors) - 1:
            self.game.explosive_brick(self)
            self.strength = 0

        self.strength -= 1
        self.color = self.game.brick_colors[self.strength]
        if self.strength == -1:
            ''' The brick has been destroyed, if it has a powerup need to
                release it.'''
            if self.powerup is not None:
                self.powerup.release_powerup(self.game, self, ball)

            self.delete(self.game)
            return False

        self.displace(self.game, self.position)
        return True
