from Parameters import *
from Object import Object
from random import randint
import time


class Ball(Object):

    def __init__(self, game, on_paddle=0):

        if on_paddle == 1:
            ''' Spawned on the paddle'''
            position = BALL["position"]
            position = [position[0] + randint(0, PADDLE["dimensions"][0]),
                        position[1]]

            super(Ball, self).__init__(game, BALL, position)
            self.is_held = True
            self.current_velocity = self.velocity
            self.is_bullet = False

        elif on_paddle == 2:
            ''' Cannon lasers'''
            self.is_bullet = True
            position = [
                game.player.paddle.position[0] +
                randint(0, 1) * game.player.paddle.dimensions[0],
                game.player.paddle.position[1] - 1]

            super(Ball, self).__init__(game, LASER, position)
            self.is_held = False
            self.current_velocity = self.velocity
        else:
            position = BALL["position"]
            position = [position[0] + randint(0, PADDLE["dimensions"][0]),
                        position[1]]

            super(Ball, self).__init__(game, BALL, position)
            self.is_held = False
            self.current_velocity = self.velocity
            self.is_bullet = False

        self.game = game

    def check_four_sides(self, new_position, game):
        ''' Of the given position, check the 4 sides of the block and see
            which ones also come under the brick.
            Order: Up, Left, Bottom, Right'''

        adj = [False, False, False, False]
        new_position = [int(new_position[0]), int(new_position[1])]
        pos = [[new_position[0], new_position[1] - 1],
               [new_position[0] - 1, new_position[1]],
               [new_position[0], new_position[1] + 1],
               [new_position[0] + 1, new_position[1]]]
        for ind in range(4):
            if adj[ind]:
                continue

            for brick in game.bricks:
                if brick.check_collision(self, pos[ind]):
                    adj[ind] = True
                    break
        return adj

    def paddle_collision(self, paddle, new_position):
        ''' relative position of the ball wrt paddles centre'''
        x_value = (new_position[0] - paddle.position[0]) -\
            paddle.dimensions[0] / 2
        relative = x_value / paddle.dimensions[0]
        assert x_value < paddle.dimensions[0]

        self.current_velocity = (relative,
                                 abs(relative) - 1)

        return paddle.catch_ball(self.game.player, self)

    def body_collision(self, body, new_position):
        ''' relative position of the ball wrt body's centre'''
        x_value = (new_position[0] - body.position[0]) -\
            body.dimensions[0] / 2
        relative = x_value / body.dimensions[0]
        assert x_value < body.dimensions[0]

        self.current_velocity = (relative,
                                 1 - abs(relative))

        return False

    def collision_side(self, brick, new_position):
        new_position = [int(new_position[0]), int(new_position[1])]
        ''' To check which side the collision happened'''
        val = ""
        ''' Checking for the 4 corners to see if its hitting the diagonal.'''
        if new_position[0] == brick.position[0] and\
                new_position[1] == brick.position[1]:
            val = "diagonal"
        elif new_position[0] == brick.position[0] and\
                new_position[1] == brick.position[1] + brick.dimensions[1]:
            val = "diagonal"
        elif new_position[0] == brick.position[0] + brick.dimensions[0] and\
                new_position[1] == brick.position[1]:
            val = "diagonal"
        elif new_position[0] == brick.position[0] + brick.dimensions[0] and\
                new_position[1] == brick.position[1] + brick.dimensions[1]:
            val = "diagonal"

        elif new_position[0] == brick.position[0] and\
                new_position[1] >= brick.position[1] and\
                new_position[1] <= (brick.position[1] + brick.dimensions[1]):
            val = "left"
        elif new_position[0] == brick.position[0] + brick.dimensions[0] and\
                new_position[1] >= brick.position[1] and\
                new_position[1] <= (brick.position[1] + brick.dimensions[1]):
            val = "right"
        elif new_position[1] >= brick.position[1] + brick.dimensions[1] and\
                new_position[0] >= brick.position[0] and\
                new_position[0] <= brick.position[0] + brick.dimensions[0]:
            val = "bottom"
        else:
            assert new_position[1] <= brick.position[1]
            assert new_position[0] >= brick.position[0]
            assert new_position[0] <= brick.position[0] + brick.dimensions[0]
            val = "top"
        return val

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
            return self.paddle_collision(other_object["value"], new_position)

        elif other_object["name"] == "body":
            ''' Collision with the boss, will damage the boss and bounce
                right back. '''
            self.game.boss.reduce_life()
            return self.body_collision(other_object["value"], new_position)

        elif other_object["name"] == "brick":
            ''' If the brick was blinking then it stops blinking'''
            other_object["value"].is_blinking = False
            is_there = len(list(filter(lambda power:
                           power["powerup"].character == "T",
                           self.game.player.powers)))

            if is_there > 0:
                return

            ''' Splits into cases on what direction it bounces off'''
            side = self.collision_side(other_object["value"],
                                       new_position)
            adjacent = other_object["adjacent"]
            if side == "diagonal":
                ''' Order: Up, Left, Bottom, Right'''

                if adjacent[1] and adjacent[3]:
                    ''' The collision was at the bottom of the slab'''
                    self.current_velocity = (self.current_velocity[0],
                                             -self.current_velocity[1])
                elif adjacent[0] and adjacent[2]:
                    ''' The collision was at the side of the platform'''
                    self.current_velocity = (-self.current_velocity[0],
                                             self.current_velocity[1])
                else:
                    sides_occupied = sum(adjacent)
                    if sides_occupied == 2:
                        ''' The diagonal'''
                        self.current_velocity = (-self.current_velocity[0],
                                                 -self.current_velocity[1])

            elif side == "bottom" or side == "top":
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

        if check_wall["name"] == "top" and self.is_bullet:
            return False

        if check_wall["name"] is not None:
            self.collision_reaction(check_wall, new_position)
            new_position = self.new_position()

        if game.player.paddle.check_collision(self, new_position):
            ''' Checking for the collision with Paddle '''
            if not self.collision_reaction({"name": "paddle",
                                            "value": game.player.paddle},
                                           new_position):
                new_position = self.new_position()
                self.displace(self.game, new_position)
                return True

        if game.level == 3 and game.boss.body.check_collision(self,
                                                              new_position):
            ''' Checking for the collision with Paddle '''
            if not self.collision_reaction({"name": "body",
                                            "value": game.boss.body},
                                           new_position):
                new_position = self.new_position()
                self.displace(self.game, new_position)
                return True

        not_collision = True
        brick_collision = False
        while not_collision:
            for brick in game.bricks:
                if brick.check_collision(self, new_position):
                    if self.is_bullet:
                        ''' Is a bullet, will only break the brick
                            and vanish'''
                        brick.is_blinking = False
                        if not brick.collision_reaction("", self):
                            ''' The brick has to be removed'''
                            if brick in game.bricks:
                                game.bricks.remove(brick)
                        return False

                    brick_collision = True
                    adjacent = self.check_four_sides(new_position, game)

                    self.collision_reaction({"name": "brick",
                                             "value": brick,
                                             "adjacent": adjacent
                                             },
                                            new_position)

                    ''' Through ball check'''
                    is_there = len(list(filter(lambda power:
                                   power["powerup"].character ==
                                   "T",
                                   game.player.powers)))
                    breakable = ""
                    if is_there > 0:
                        breakable = "OP"
                    self.game.player.score_increase(brick.strength)
                    if not brick.collision_reaction(breakable, self):
                        ''' The brick has to be removed'''
                        if brick in game.bricks:
                            game.bricks.remove(brick)

                    if is_there == 0:
                        new_position = self.new_position()
                        not_collision = False

            for brick in game.bricks:
                if brick.strength == -1:
                    if brick.powerup is not None:
                        brick.powerup.release_powerup(game, brick, self)
                    brick.delete(game)

            if not not_collision:
                ''' Position was updated, hence there is a need to
                    check the new position again if it's colliding in the
                    new location too'''
                not_collision = True
            else:
                ''' Collision did not happen at all so can move on'''
                break

        self.displace(self.game, new_position)

        ''' Shifting all the bricks by 1 if the time has crossed some value'''
        time_diff = time.time() - self.game.player.init_time
        if time_diff >= BRICK_SHIFT and brick_collision and game.level < 3:
            self.game.shift_bricks()

        return True

    def paddle_release(self):
        self.is_held = False

    def paddle_held(self):
        self.is_held = True
