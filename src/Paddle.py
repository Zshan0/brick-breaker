from Parameters import *
from Object import Object


class Paddle(Object):

    def __init__(self, game, ball):

        super(Paddle, self).__init__(game, PADDLE, PADDLE["position"])
        self.is_holding = ball

    def collision_reaction(self, other_object):
        ''' Sends the object with which it is going to collide.
            If the object's name is Boundary it is the walls'''

        if other_object["name"] == "Boundary":
            return

    def move_paddle(self, game, value):
        ''' Since the paddle will only move either left or right, the value
            will be -1, 0 or 1.'''
        new_position = [self.position[0] + (value * self.velocity[0]),
                        self.position[1]]

        check_wall = self.check_wall(game, new_position)

        if check_wall["name"] is not None:
            return

        self.displace(game, new_position)

        if self.is_holding is not None:
            ''' Need to move the ball which is held by the same
                distance'''
            ball_position = self.is_holding.position
            ball_position = [ball_position[0] + value * self.velocity[0],
                             ball_position[1]]

            self.is_holding.displace(game, ball_position)

    def release_ball(self):
        if self.is_holding is not None:
            self.is_holding.paddle_release()

        self.is_holding = None

    def catch_ball(self, player, ball):
        if "catch" in player.powers:
            ''' The player is able to catch the ball'''
            self.is_holding = ball
            ball.paddle_held()
