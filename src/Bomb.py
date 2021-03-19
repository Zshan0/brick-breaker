from Parameters import *
from Object import Object
from random import randint


class Bomb(Object):

    def __init__(self, game):

        position = BOMB["position"]

        super(Bomb, self).__init__(game, BOMB, position)
        self.game = game
        self.prev_color = game.background_color + ' ' + RESET

    def move_bomb(self, game):

        ''' Removing the old position and replacing it old value'''
        cur_pos = [int(self.position[0]) + game.origin[0],
                   int(self.position[1]) + game.origin[1]]

        game.screen.screen_string[cur_pos[1]][cur_pos[0]] = self.prev_color

        ''' Putting the powerup at the new position'''
        new_position = [self.position[0] + self.velocity[0],
                        self.position[1] + self.velocity[1]]

        check_wall = self.check_wall(game, new_position)

        if check_wall["name"] == "bottom":
            return False

        if game.player.paddle.check_collision(self, new_position):
            game.player.reduce_life()
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
