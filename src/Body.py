from Parameters import *
from Object import Object


class Body(Object):

    def __init__(self, game):
        super(Body, self).__init__(game, BODY, BODY["position"])
        self.game = game

    def collision_reaction(self, other_object):
        ''' Sends the object with which it is going to collide.
            If the object's name is Boundary it is the walls'''

        if other_object["name"] == "Boundary":
            return

    def move_body(self, game, value):
        ''' Since the paddle will only move either left or right, the value
            will be -1, 0 or 1.'''
        new_position = [self.position[0] + int(value * self.velocity[0]),
                        self.position[1]]

        check_wall = self.check_wall(game, new_position)

        if check_wall["name"] is not None:
            return

        self.displace(game, new_position)
