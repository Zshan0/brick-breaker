from Parameters import *
import random
from Brick import Brick
from Boss import Boss
import time


class Game:
    def __init__(self, screen, menu, top, border, level):
        """Putting all the required components the in the game modules
        for ease of access."""
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
        self.max_explosive = GAME["max_explosive"]
        self.bricks = []
        self.level = level

    def set_boss(self):
        """ Boss moves in the same direction as the player """
        boss = Boss(self)
        self.boss = boss

    def set_player(self, player):
        self.player = player

    def set_bricks(self, region=None, is_boss=False):
        if region is None:
            region = self.brick_region

        max_brick_row = int(self.dimensions[0] / (self.brick_size[0] + 1))
        bricks_so_far = 0

        explosive_row = random.randint(region[0], region[1] - 1)
        explosive_bricks = 0

        for row in range(region[0], region[1]):
            for brick in range(max_brick_row):
                coords = (
                    brick * (self.brick_size[0] + 1),
                    row * (self.brick_size[1] + 1),
                )

                if (
                    row == explosive_row
                    and explosive_bricks < self.max_explosive
                ):
                    brick = Brick(self, len(self.brick_colors) - 2, coords)
                    self.bricks.append(brick)
                    bricks_so_far += 1
                    explosive_bricks += 1

                else:
                    is_brick = (random.randint(0, 1)) == 0
                    if is_brick:
                        if is_boss:
                            strength = random.randint(
                                0,
                                len(self.brick_colors) - 3)
                        else:
                            strength = random.randint(
                                0,
                                len(self.brick_colors) - 2)

                        brick = Brick(self, strength, coords)
                        self.bricks.append(brick)
                        bricks_so_far += 1

                if bricks_so_far == self.max_bricks:
                    break
            else:
                continue
            break

    def delete_bricks(self):
        ''' Clearing out all the bricks and returning
            the original positions'''
        for brick in self.bricks:
            brick.delete(self)
        return self.bricks

    def shift_bricks(self, shift_val=1):
        ''' Shifting all the bricks by the given value and displaying
            them'''
        for brick in self.bricks[::-1]:
            new_pos = [
                brick.position[0],
                brick.position[1] + shift_val
            ]
            brick.displace(self, new_pos)

    def explosive_brick(self, brick):
        """ The passed brick is deleted anyway"""
        cur_pos = brick.position
        left_pos = [cur_pos[0] - (brick.dimensions[0] + 1), cur_pos[1]]
        right_pos = [cur_pos[0] + (brick.dimensions[0] + 1), cur_pos[1]]
        up_pos = [cur_pos[0], cur_pos[1] - (brick.dimensions[1] + 1)]
        down_pos = [cur_pos[0], cur_pos[1] + (brick.dimensions[1] + 1)]

        up_left_pos = [left_pos[0], up_pos[1]]
        up_right_pos = [right_pos[0], up_pos[1]]
        down_left_pos = [left_pos[0], down_pos[1]]
        down_right_pos = [right_pos[0], down_pos[1]]

        brick_pos = [
            left_pos,
            right_pos,
            up_pos,
            down_pos,
            up_left_pos,
            up_right_pos,
            down_left_pos,
            down_right_pos,
        ]

        for brick in self.bricks:

            for req_brick in brick_pos:
                if req_brick[0] == brick.position[0]:
                    if req_brick[1] == brick.position[1]:
                        if brick.strength == len(self.brick_colors) - 1:
                            continue

                        brick.collision_reaction("OP")
                        if brick in self.bricks:
                            self.bricks.remove(brick)

    def boss_check(self):
        if self.boss.lives == 0:
            self.player.game_over()
        if self.player.lives == 0:
            self.player.game_over()

    def bricks_check(self):
        breakable_bricks = list(
            filter(
                lambda x: x.strength != len(self.brick_colors) - 2, self.bricks
            )
        )
        if len(breakable_bricks) == 0:
            ''' Completes the level and moves on the next level'''
            return True
        if self.player.lives == 0:
            self.player.game_over()

        ''' Checking if a brick is on the same level as the paddle'''
        for brick in self.bricks:
            brick.blink()
            if brick.strength == len(self.brick_colors) - 2:
                ''' If unbreakable bricks then fine'''
                continue
            if brick.position[1] + brick.dimensions[1] ==\
                    self.player.paddle.position[1]:
                self.player.game_over()

    def game_over(self):
        self.top.display_game_over(self.screen)

    def set_lives(self, lives):
        self.top.set_lives(self.screen, lives)

    def set_boss_bar(self, lives):
        self.top.set_boss_bar(self.screen, lives)

    def set_level(self):
        self.top.set_level(self.screen, self.level)

    def test_output(self):
        """ To quickly check if the colors fit the palette"""
        print(GAME["background_color"] + "background_color" + RESET)
        for i in range(len(GAME["brick_colors"])):
            print("{} brick {} {}".format(GAME["brick_colors"][i], i, RESET))
        print("{} paddle {}".format(GAME["paddle_color"], RESET))

    def reset_screen(self):
        ''' Resetting the complete screen after some frames to remove glitches '''
        background = self.background_color + " " + RESET

        start_pos = [self.origin[0], self.origin[1]]
        end_pos = [
            self.origin[0] + self.dimensions[0],
            self.origin[1] + self.dimensions[1],
        ]
        self.screen.fill_screen(start_pos, end_pos, background)
        self.border.set_screen(self.screen)
        for ball in self.player.balls:
            ball.displace(self, ball.position)

        self.shift_bricks(0)
        self.player.paddle.displace(self, self.player.paddle.position)
        if self.level == 3:
            self.boss.body.displace(self, self.boss.body.position)

    def set_screen(self):
        """ resets the screen according to the new values"""
        self.menu.set_screen(self.screen)
        self.top.set_screen(self.screen)
        self.border.set_screen(self.screen)
        background = self.background_color + " " + RESET

        start_pos = [self.origin[0], self.origin[1]]
        end_pos = [
            self.origin[0] + self.dimensions[0],
            self.origin[1] + self.dimensions[1],
        ]

        self.screen.fill_screen(start_pos, end_pos, background)
