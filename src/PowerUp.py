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

    def release_powerup(self, game):
        self.prev_color = game.background_color + ' ' + RESET
        self.is_visible = True

        new_pos = [self.position[0] + self.velocity[0],
                   self.position[1] + self.velocity[1]]
        self.position = new_pos
        game.player.powerups.append(self)
        # self.displace(game, new_pos)

    def move_powerup(self, game):

        ''' Removing the old position and replacing it old value'''
        start_pos = [int(self.position[0]) + game.origin[0],
                     int(self.position[1]) + game.origin[1]]
        end_pos = [start_pos[0] + self.dimensions[0],
                   start_pos[1] + self.dimensions[1]]
        background_color = self.prev_color

        game.screen.fill_screen(start_pos, end_pos, background_color)

        ''' Putting the powerup at the new position'''
        new_position = [self.position[0] + self.velocity[0],
                        self.position[1] + self.velocity[1]]

        check_wall = self.check_wall(game, new_position)

        if check_wall["name"] == "bottom":
            return False

        if game.player.paddle.check_collision(self, new_position):
            game.player.powerup_gain(self)
            return False

        start_pos = [int(self.position[0] + self.velocity[0]) + game.origin[0],
                     int(self.position[1] + self.velocity[1]) + game.origin[1]]
        end_pos = [start_pos[0] + self.dimensions[0],
                   start_pos[1] + self.dimensions[1]]

        background_color = self.color + self.character + RESET
        self.prev_color = game.screen.screen_string[start_pos[1]][start_pos[0]]

        game.screen.fill_screen(start_pos, end_pos, background_color)

        self.position = new_position
        return True






