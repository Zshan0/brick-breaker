from Parameters import *


class Object():

    def __init__(self, game, desc, position):
        ''' It is assumed that the position is relative to origin
            of the screen.'''
        self.name = desc["name"]
        self.color = desc["color"]
        self.dimensions = desc["dimensions"]
        self.velocity = desc["velocity"]
        self.position = position
        self.character = ' '

        ''' setting the object onto the given position'''
        origin = GAME["origin"]
        start_pos = [origin[0] + position[0],
                     origin[1] + position[1]]
        end_pos = [start_pos[0] + self.dimensions[0],
                   start_pos[1] + self.dimensions[1]]
        if "character" in desc:
            self.character = desc["character"]
            color = self.color + desc["character"] + RESET
        else:
            color = self.color + ' ' + RESET

        game.screen.fill_screen(start_pos, end_pos, color)

    def check_wall(self, game, new_position):
        ''' Checks if the object is going to cross the walls and returns
            left, right, up, bottom or None'''
        dimensions = game.dimensions
        val = ""
        if int(new_position[0]) < 0:
            val = "left"
        elif int(new_position[1]) < 0:
            val = "top"
        elif int(new_position[0] + self.dimensions[0]) >= int(dimensions[0]):
            val = "right"
        elif int(new_position[1] + self.dimensions[1]) >= int(dimensions[1]):
            val = "bottom"
        else:
            val = None
        return {"name": val}

    def check_collision(self, other_object, new_position):
        ''' To check if the other object passed is colliding
            with the object which called this function.
            New position is the position at which other_object is going
            to be in.'''

        ''' Collision for the ball'''
        if other_object.name == "ball" or\
           other_object.name == "powerup" or\
           other_object.name == "bomb" or\
           other_object.name == "laser":

            if int(new_position[1]) >= int(self.position[1]) and\
                    int(new_position[1]) <=\
                    int(self.position[1] + self.dimensions[1]):
                ''' y value matches, have to check for x value'''

                if int(new_position[0]) >= int(self.position[0]) and\
                        int(new_position[0]) <=\
                        int(self.position[0] + self.dimensions[0]):
                    return True

            return False


    def delete(self, game):
        ''' Call before to reset the background before deleting the object'''
        start_pos = [int(self.position[0]) + game.origin[0],
                     int(self.position[1]) + game.origin[1]]
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
        start_pos = [int(new_position[0]) + game.origin[0],
                     int(new_position[1]) + game.origin[1]]
        end_pos = [start_pos[0] + self.dimensions[0],
                   start_pos[1] + self.dimensions[1]]
        object_color = self.color + self.character + RESET

        self.position = new_position
        game.screen.fill_screen(start_pos, end_pos, object_color)
