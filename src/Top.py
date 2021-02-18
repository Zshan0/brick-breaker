from Parameters import *


class Top:

    def test_output(self):
        print(TOP["background_color"] + "background_color" + RESET)
        print(TOP["text_color"] + "text_color" + RESET)
        print(TOP["heart_color"] + TOP["heart_icon"] + RESET)
        print(TOP["time_color"] + TOP["time_icon"] + RESET)

    def set_lives(self, screen, player_lives=-1):
        ''' displaying the icon and the number of lives left
            if lives == -1 then the TOP is not in progress.'''

        # USE ORIGIN
        icon = TOP["heart_icon"]
        pos = TOP["heart_pos"]
        origin = TOP["origin"]
        text_color = TOP["text_color"]
        lives = icon
        if player_lives == -1:
            lives += ' -'
        else:
            lives += ' ' + str(int(player_lives))

        for x in range(len(lives)):
            screen.screen_string[origin[1] + pos[1]][origin[0] + pos[0] + x] =\
                text_color + lives[x] + RESET

    def set_time(self, screen, player_time=-1):
        ''' displaying the icon and the amount of time that has passed.
            if time == -1 then the TOP is not in progress.'''

        # USE ORIGIN
        origin = TOP["origin"]
        icon = TOP["time_icon"]
        pos = TOP["time_pos"]
        text_color = TOP["text_color"]
        time = icon
        if player_time == -1:
            time += ' -'
        else:
            time += ' ' + str(int(player_time))
        screen.screen_string[2][origin[0] + pos[0]] = 'A'
        for x in range(len(time)):
            screen.screen_string[origin[1] + pos[1]][origin[0] + pos[0] + x] =\
                text_color + time[x] + RESET

    def display_game_over(self, screen):
        origin = TOP["origin"]
        pos = TOP["game_over_pos"]
        text = TOP["game_over_text"]
        text_color = TOP["text_color"]

        for x in range(len(text)):
            screen.screen_string[origin[1] + pos[1]][origin[0] + pos[0] + x] =\
                text_color + text[x] + RESET
        self.set_lives(screen, -1)
        self.set_time(screen, -1)

    def set_screen(self, screen):
        background = TOP["background_color"] + ' ' + RESET
        start_pos = [TOP["origin"][0],
                     TOP["origin"][1]]
        end_pos = [TOP["origin"][0] + TOP["dimensions"][0],
                   TOP["origin"][1] + TOP["dimensions"][1]]

        screen.fill_screen(start_pos, end_pos, background)
        self.set_lives(screen)
        self.set_time(screen)
