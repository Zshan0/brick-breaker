from Parameters import *
import random
from Brick import Brick
import time

class Game:

    def __init__(self, screen, menu, top, border):
        ''' Putting all the required components the in the game modules
            for ease of access.'''
        self.screen = screen
        self.menu = menu
        self.top = top
        self.border = border
        self.dimensions = GAME["dimensions"]
        self.origin = GAME["origin"]
        self.background_color = GAME["background_color"]
        self.brick_colors = GAME["brick_colors"]
        self.brick_region = GAME["brick_region"]
        self.brick_size = BRICK["dimensions"]
        self.max_bricks = GAME["max_bricks"]
        self.bricks = []

    def set_player(self, player):
        self.player = player

    def set_bricks(self):
        region = self.brick_region

        max_brick_row = int(self.dimensions[0] / (self.brick_size[0] + 1))
        bricks_so_far = 0

        for row in range(region[0], region[1]):
            for brick in range(max_brick_row):
                coords = (brick * (self.brick_size[0] + 1), row *
                          (self.brick_size[1] + 1))

                is_brick = (random.randint(0, 1)) == 0
                if is_brick:
                    strength = random.randint(0, len(self.brick_colors) - 1)
                    brick = Brick(self, strength, coords)
                    self.bricks.append(brick)

                    bricks_so_far += 1
                    if bricks_so_far == self.max_bricks:
                        break
            else:
                continue
            break

    def explosive_brick(self, brick):
        ''' The passed brick is deleted anyway'''
        cur_pos = brick.position
        left_pos = [cur_pos[0] - (brick.dimensions[0] + 1),
                    cur_pos[1]]
        right_pos = [cur_pos[0] + (brick.dimensions[0] + 1),
                     cur_pos[1]]
        up_pos = [cur_pos[0],
                  cur_pos[1] - (brick.dimensions[1] + 1)]
        down_pos = [cur_pos[0],
                    cur_pos[1] + (brick.dimensions[1] + 1)]

        up_left_pos = [left_pos[0], up_pos[1]]
        up_right_pos = [right_pos[0], up_pos[1]]
        down_left_pos = [left_pos[0], down_pos[1]]
        down_right_pos = [right_pos[0], down_pos[1]]

        brick_pos = [left_pos, right_pos, up_pos, down_pos, up_left_pos,
                     up_right_pos, down_left_pos, down_right_pos]

        for brick in self.bricks:

            for req_brick in brick_pos:
                if req_brick[0] == brick.position[0]:
                    if req_brick[1] == brick.position[1]:

                        brick.collision_reaction("OP")
                        if brick in self.bricks:
                            self.bricks.remove(brick)


    def game_over(self):
        self.top.display_game_over(self.screen)

    def set_lives(self, lives):
        self.top.set_lives(self.screen, lives)

    def test_output(self):
        ''' To quickly check if the colors fit the palette'''
        print(GAME["background_color"] + "background_color" + RESET)
        for i in range(len(GAME["brick_colors"])):
            print("{} brick {} {}".format(GAME["brick_colors"][i],  i, RESET))
        print("{} paddle {}".format(GAME["paddle_color"], RESET))

    def set_screen(self):
        ''' resets the screen according to the new values'''
        self.menu.set_screen(self.screen)
        self.top.set_screen(self.screen)
        self.border.set_screen(self.screen)
        background = self.background_color + ' ' + RESET

        start_pos = [self.origin[0],
                     self.origin[1]]
        end_pos = [self.origin[0] + self.dimensions[0],
                   self.origin[1] + self.dimensions[1]]

        self.screen.fill_screen(start_pos, end_pos, background)
