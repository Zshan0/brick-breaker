from Parameters import *


class Border:

    def test_output(self):
        print("{} border color {}".format(BORDER["color"], RESET))

    def set_screen(self, screen):
        color = BORDER["color"] + ' ' + RESET

        for wall in BORDER["dimensions"]:
            ''' fills the walls with the color'''
            screen.fill_screen(wall[0], wall[1], color)
