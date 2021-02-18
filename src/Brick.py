from Parameters import *
from Object import Object


class Brick(Object):
    def __init__(self, game, strength, position):
        desc = BRICK
        desc.update({"color": game.brick_colors[strength]})
        super(Brick, self).__init__(game, desc, position)
        self.strength = strength
        self.game = game
        self.color = game.brick_colors[strength]

    def collision_reaction(self, other_object):

        if other_object.name == "power":
            ''' Do nothing if powerup is colliding, just let it pass'''
            return
        ''' The only other collision that can happen is the ball collision'''
        assert other_object.name == "ball"

        if self.strength == len(self.game.brick_colors) - 1:
            ''' Maximum Strength ones can't be broken'''
            return True

        self.strength -= 1
        self.color = self.game.brick_colors[self.strength]
        if self.strength == -1:
            self.delete(self.game)
            return False

        self.displace(self.game, self.position)
        return True
