import pygame
import GameObject
from gameobjects.objects import Button

class UserProfileScreen(GameObject.GameObject):
    def __init__(self):
        super().__init__(20)

        self.background_image = pygame.image.load("media/start/ProfileScreen.png").convert_alpha()
        self.menu1_image = pygame.image.load("media/start/MenuProfile.png").convert_alpha()
        self.menu2_image = pygame.image.load("media/start/MenuProfile.png").convert_alpha()
        self.menu3_image = pygame.image.load("media/start/MenuProfile.png").convert_alpha()

        self.background_x = 100
        self.background_y = 50

    def draw(self, game_display):
        pass

    def handle_input(self, stage, events):
        pass

    def step(self, stage):
        pass

    def load_profiles(self):
        profile1 = open("profile1.txt")
        profile2 = open("profile2.txt")
        profile3 = open("profile3.txt")