class Object:

    def __init__(self, screen, x, y):
        self.position = {"x": x, "y": y}
        self.value = 1
        screen.screen_string[y][x] = self.value

    def update_position(self, screen, x, y):
        screen.screen_string[self.position["y"]][self.position["x"]] = 0
        screen.screen_string[y][x] = self.value
        self.position = {"x": x, "y": y}
