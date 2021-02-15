from Parameters import *
from Object import Object


class Ball(Object):

    def __init__(self, game):

        super(Ball, self).__init__(game, BALL, BALL["position"])
        self.is_held = False
        self.current_velocity = self.velocity

    def collision_reaction(self, other_object, game):
        ''' Sends the object with which it is going to collide.
            If the object's name is Boundary it is the walls'''

        if other_object["name"] == "left" or other_object["name"] == "right":
            ''' Collision with the vertical walls'''
            self.current_velocity = (-self.current_velocity[0],
                                     self.current_velocity[1])

        elif other_object["name"] == "top":
            ''' Collision with the top wall'''
            self.current_velocity = (self.current_velocity[0],
                                     -self.current_velocity[1])
        elif other_object["name"] == "bottom":
            # super(Ball, self).delete(game, BALL, BALL["position"])
            self.delete(game)

        elif other_object["name"] == "paddle":
            pass
        elif other_object["name"] == "brick":
            ''' Splits into cases on what direction it bounces off'''
            pass

    def new_position(self):
        ''' Function which returns the displaced position of the object'''
        return [self.position[0] + self.current_velocity[0],
                self.position[1] + self.current_velocity[1]]

    def paddle_release(self):
        self.is_held = False

    def paddle_held(self):
        self.is_held = True
