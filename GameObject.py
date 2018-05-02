import pygame


class GameObject(object):
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    RESOLUTION = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

    def __init__(self, z_index = 0):
        self.z_index = z_index
        self.hidden = False
        self.ignore_input = False


    def draw(self, game_display):
        print("Error!  Not implemented.")

    def handle_input(self, stage, events):
        print("Error!  Not implemented.")

    def step(self, stage):
        pass

    def set_active(self):
        self.hidden = False
        self.ignore_input = False

    def set_inactive(self):
        self.hidden = True
        self.ignore_input = True