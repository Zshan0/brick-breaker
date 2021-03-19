from Parameters import *
from Object import Object


class PowerUp(Object):

    def __init__(self, powerup, position):

        self.powerup = powerup
        self.name = POWERUP["name"]
        self.color = POWERUP["color"]
        self.dimensions = POWERUP["dimensions"]
        self.velocity = POWERUP["velocity"]
        self.position = position
        self.character = POWERUP["text"][powerup]
        self.is_visible = False
        self.prev_color = None

    def release_powerup(self, game, brick, ball):
        self.prev_color = game.background_color + ' ' + RESET
        self.is_visible = True
        if ball is not None:
            self.velocity = [ball.velocity[0], -abs(ball.velocity[1])]

        new_pos = [brick.position[0] + self.velocity[0],
                   brick.position[1] + self.velocity[1]]
        self.position = new_pos
        game.player.powerups.append(self)
        # self.displace(game, new_pos)

    def move_powerup(self, game):

        ''' Removing the old position and replacing it old value'''
        self.velocity = [self.velocity[0], min(self.velocity[1] + GRAVITY, 1)]
        cur_pos = [int(self.position[0]) + game.origin[0],
                   int(self.position[1]) + game.origin[1]]

        game.screen.screen_string[cur_pos[1]][cur_pos[0]] = self.prev_color

        ''' Gravity Effects'''
        # self.velocity = [self.velocity[0], self.velocity[1] + GRAVITY]

        ''' Putting the powerup at the new position'''
        new_position = [self.position[0] + self.velocity[0],
                        self.position[1] + self.velocity[1]]

        check_wall = self.check_wall(game, new_position)

        if check_wall["name"] == "left" or check_wall["name"] == "right":
            ''' Collision with the vertical walls'''
            self.elocity = (-self.velocity[0],
                                     self.velocity[1])

        elif check_wall["name"] == "top":
            ''' Collision with the top wall'''
            self.velocity = (self.velocity[0],
                                     -self.velocity[1])


        if check_wall["name"] == "bottom":
            return False

        if game.player.paddle.check_collision(self, new_position):
            game.player.powerup_gain(self)
            return False

        self.prev_color = game.background_color + ' ' + RESET

        start_pos = [int(self.position[0] + self.velocity[0]) + game.origin[0],
                     int(self.position[1] + self.velocity[1]) + game.origin[1]]

        for brick in game.bricks:
            if brick.check_collision(self, new_position):
                self.prev_color = game.screen.screen_string[start_pos[1]
                                                            ][start_pos[0]]
                break

        new_color = self.color + self.character + RESET

        game.screen.screen_string[start_pos[1]][start_pos[0]
                                                ] = new_color

        self.position = new_position
        return True







