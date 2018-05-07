import pygame


class GameObject(object):
    DISPLAY_WIDTH = 800
    DISPLAY_HEIGHT = 600
    RESOLUTION = (DISPLAY_WIDTH, DISPLAY_HEIGHT)
    pygame.font.init()
    FONT_12 = pygame.font.Font("media/start/big_noodle_titling.ttf", 12)
    FONT_20 = pygame.font.Font("media/start/big_noodle_titling.ttf", 20)
    FONT_24 = pygame.font.Font("media/start/big_noodle_titling.ttf", 24)
    FONT_48 = pygame.font.Font("media/start/big_noodle_titling.ttf", 48)
    FONT_64 = pygame.font.Font("media/start/big_noodle_titling.ttf", 64)

    def __init__(self, z_index = 0, has_music=False):
        self.z_index = z_index
        self.hidden = False
        self.ignore_input = False
        self.has_music = has_music

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