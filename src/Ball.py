from Parameters import *
from Object import Object


class Ball(Object):

    def __init__(self, game):

        super(Ball, self).__init__(game, BALL, BALL["position"])
        self.is_held = False
        self.current_velocity = self.velocity
        self.game = game

    def collision_side(self, brick, new_position):
        ''' To check which side the collision happened'''
        if new_position[0] == brick.position[0] and\
                new_position[1] <= (brick.position[1] + brick.dimensions[1]):
            return "left"
        elif new_position[0] == brick.position[0] + brick.dimensions[0] and\
                new_position[1] <= (brick.position[1] + brick.dimensions[1]):
            return "right"
        elif new_position[1] >= brick.position[1] + brick.dimensions[1]:
            return "bottom"

        assert new_position[1] <= brick.position[1]
        return "top"

    def collision_reaction(self, other_object, new_position):
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
            self.delete(self.game)

        elif other_object["name"] == "paddle":
            ''' It is assumed that the collision is happening at the top
                of the paddle only, side ones are also taken to be top.
                '''
            self.current_velocity = (self.current_velocity[0],
                                     -self.current_velocity[1])
        elif other_object["name"] == "brick":
            ''' Splits into cases on what direction it bounces off'''
            side = self.collision_side(other_object["value"],
                                       new_position)

            if side == "bottom" or side == "top":
                self.current_velocity = (self.current_velocity[0],
                                         -self.current_velocity[1])
            else:
                self.current_velocity = (-self.current_velocity[0],
                                         self.current_velocity[1])

    def new_position(self):
        ''' Function which returns the displaced position of the object'''
        return [self.position[0] + self.current_velocity[0],
                self.position[1] + self.current_velocity[1]]

    def move_ball(self, game):
        new_position = self.new_position()

        check_wall = self.check_wall(self.game, new_position)
        if check_wall["name"] == "bottom":
            ''' The ball has to be deleted.'''
            return False

        if check_wall["name"] is not None:
            print(check_wall["name"])
            self.collision_reaction(check_wall, new_position)
            new_position = self.new_position()

        if game.player.paddle.check_collision(self, new_position):
            ''' Checking for the collision with Paddle '''
            self.collision_reaction({"name": "paddle",
                                     "value": game.player.paddle},
                                    new_position)
            new_position = self.new_position()

        self.displace(self.game, new_position)
        return True

    def paddle_release(self):
        self.is_held = False

    def paddle_held(self):
        self.is_held = True
