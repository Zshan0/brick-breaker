from Parameters import *


class Top:

    def test_output(self):
        print(TOP["background_color"] + "background_color" + RESET)
        print(TOP["text_color"] + "text_color" + RESET)
        print(TOP["heart_color"] + TOP["heart_icon"] + RESET)
        print(TOP["time_color"] + TOP["time_icon"] + RESET)

    def __init__(self):
        self.lives = -1
        self.score = -1
        self.time = -1

    def set_lives(self, screen):
        ''' displaying the icon and the number of lives left
            if lives == -1 then the game is not in progress.'''

        # USE ORIGIN
        icon = TOP["heart_icon"]
        pos = TOP["heart_pos"]
        text_color = TOP["text_color"]
        lives = icon
        if self.lives == -1:
            lives += ' -'
        else:
            lives += ' ' + str(int(self.lives))

        for x in range(len(lives)):
            screen.screen_string[pos[1]][pos[0] + x] = \
                text_color + lives[x] + RESET

    def set_time(self, screen):
        ''' displaying the icon and the amount of time that has passed.
            if time == -1 then the game is not in progress.'''

        # USE ORIGIN
        icon = TOP["time_icon"]
        pos = TOP["time_pos"]
        text_color = TOP["text_color"]
        time = icon
        if self.time == -1:
            time += ' -'
        else:
            time += ' ' + str(int(self.time))

        for x in range(len(time)):
            screen.screen_string[pos[1]][pos[0] + x] = \
                text_color + time[x] + RESET

    def set_screen(self, screen):
        background = TOP["background_color"] + ' ' + RESET
        origin = TOP["origin"]
        dimensions = TOP["dimensions"]

        for x in range(origin[0], dimensions[0]):
            for y in range(origin[1], dimensions[1]):
                screen.screen_string[y][x] = background

        # self.set_lives(screen)
        self.set_time(screen)
