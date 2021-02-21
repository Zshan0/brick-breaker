from Parameters import *
from Object import Object


class Paddle(Object):

    def __init__(self, game, ball):
        super(Paddle, self).__init__(game, PADDLE, PADDLE["position"])
        self.is_holding = ball
        ball.paddle_held()
        self.game = game

    def collision_reaction(self, other_object):
        ''' Sends the object with which it is going to collide.
            If the object's name is Boundary it is the walls'''

        if other_object["name"] == "Boundary":
            return

    def move_paddle(self, game, value):
        ''' Since the paddle will only move either left or right, the value
            will be -1, 0 or 1.'''
        new_position = [self.position[0] + int(value * self.velocity[0]),
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
        self.displace(self.game, self.position)

    def catch_ball(self, player, ball):
        is_there = len(list(filter(lambda power:
                                   power["powerup"].character ==
                                   "P",
                                   player.powers)))

        if is_there > 0 and self.is_holding is None:
            ''' The player is able to catch the ball'''
            self.is_holding = ball
            ball.paddle_held()
            return True
        return False

    def expand_paddle(self, player):
        self.dimensions = [self.dimensions[0] + PADDLE["change"],
                           self.dimensions[1]]
        self.displace(player.game, self.position)

    def shrink_paddle(self, player):
        self.delete(player.game)
        self.dimensions = [self.dimensions[0] - PADDLE["change"],
                           self.dimensions[1]]
        self.displace(player.game, self.position)


