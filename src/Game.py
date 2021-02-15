from Parameters import *


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

    def set_player(self, player):
        self.player = player

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
