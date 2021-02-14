from Parameters import *


class Menu:

    def test_output(self):
        print(MENU["background_color"] + "background_color" + RESET)
        print(MENU["text_color"] + "text_color" + RESET)

    def set_name(self, screen):
        name_pos = MENU["name_pos"]
        text_color = MENU["text_color"]
        name = MENU["name"]

        for i in range(len(name)):
            screen.screen_string[name_pos[1]][name_pos[0] + i] = \
                text_color + name[i] + RESET

    def set_options(self, screen, player_option):
        options = MENU["options"]
        options_pos = MENU["options_pos"]
        options_color = MENU["options_color"]
        selected_option_color = MENU["selected_option_color"]

        for option_num in range(len(options)):
            cur_option = options[option_num]
            cur_pos = options_pos[option_num]
            if option_num == player_option:
                color = selected_option_color
            else:
                color = options_color

            for i in range(len(cur_option)):
                screen.screen_string[cur_pos[1]][cur_pos[0] + i] = \
                    color + cur_option[i] + RESET

    def set_screen(self, screen, player_option=0):
        background = MENU["background_color"] + ' ' + RESET
        start_pos = [MENU["origin"][0],
                     MENU["origin"][1]]
        end_pos = [MENU["origin"][0] + MENU["dimensions"][0],
                   MENU["origin"][1] + MENU["dimensions"][1]]

        screen.fill_screen(start_pos, end_pos, background)
        self.set_name(screen)
        self.set_options(screen, player_option)
