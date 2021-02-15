from Parameters import *
from Game import Game


class Object():

    def __init__(self, game, desc, position):
        ''' It is assumed that the position is relative to origin
            of the screen.'''
        self.name = desc["name"]
        self.color = desc["color"]
        self.dimensions = desc["dimensions"]
        self.velocity = desc["velocity"]
        self.position = position

        ''' setting the object onto the given position'''
        origin = GAME["origin"]
        start_pos = [origin[0] + position[0],
                     origin[1] + position[1]]
        end_pos = [start_pos[0] + self.dimensions[0],
                   start_pos[1] + self.dimensions[1]]
        color = self.color + ' ' + RESET
        game.screen.fill_screen(start_pos, end_pos, color)

    def check_wall(self, game, new_position):
        ''' Checks if the object is going to cross the walls and returns
            left, right, up, bottom or None'''
        dimensions = game.dimensions
        val = ""
        if new_position[0] < 0:
            val = "left"
        elif new_position[1] < 0:
            val = "up"
        elif (new_position[0] + self.dimensions[0]) >= dimensions[0]:
            val = "right"
        elif (new_position[1] + self.dimensions[1]) >= dimensions[1]:
            val = "bottom"
        else:
            val = None
        return {"name": val}

    def check_collision(self, other_object):
        ''' To check if the other object passed is colliding
            with the object which called this function'''

        def inside_box(self, coords):
            ''' To check if (x, y) are inside the object '''
            (x, y) = coords
            x_check = (self.position[0] <= x) and \
                ((self.position[0] + self.dimensions[0]) >= x)

            y_check = (self.position[1] <= y) and \
                ((self.position[1] + self.dimensions[1]) >= y)
            return x_check and y_check

        def get_corners(position, dimensions):
            ''' Returning the corners of the object whose position and
                dimensions are given. All the objects are rectangle'''
            coords = [[position[0],
                       position[1]],

                      [position[0] + dimensions[0],
                       position[1]],

                      [position[0],
                       position[1] + dimensions[1]],

                      [position[0] + dimensions[0],
                       position[1] + dimensions[1]]]
            return coords

        coords = get_corners(other_object.position, other_object.dimensions)

        for coord in coords:
            if inside_box(self, coord):
                return True

        return False

    def delete(self, game):
        ''' Call before to reset the background before deleting the object'''
        start_pos = [self.position[0] + game.origin[0],
                     self.position[1] + game.origin[1]]
        end_pos = [start_pos[0] + self.dimensions[0],
                   start_pos[1] + self.dimensions[1]]
        background_color = game.background_color + ' ' + RESET

        game.screen.fill_screen(start_pos, end_pos, background_color)

    def displace(self, game, new_position):
        ''' Given object is removed from its current position and
            moved to the new given position. It is assumed that there are
            no collisions. The coordinates are relative to game origin'''

        ''' Replacing the original one with background '''
        self.delete(game)

        ''' Putting the object to the new location '''
        start_pos = [new_position[0] + game.origin[0],
                     new_position[1] + game.origin[1]]
        end_pos = [start_pos[0] + self.dimensions[0],
                   start_pos[1] + self.dimensions[1]]
        object_color = self.color + ' ' + RESET

        game.screen.fill_screen(start_pos, end_pos, object_color)
        self.position = new_position
