import pygame
import GameObject
from gameobjects.objects import Button


class UserProfileScreen(GameObject.GameObject):

    def __init__(self):
        super().__init__(5)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/user_profile_menu.png").convert_alpha()
        self.USER_SLOT1 = pygame.image.load("media/start/profile_option.png").convert_alpha()
        self.USER_SLOT1_COORDS = (100, 200)
        self.USER_SLOT2 = pygame.image.load("media/start/profile_option.png").convert_alpha()
        self.USER_SLOT2_COORDS = (100, 350)
        self.USER_SLOT3 = pygame.image.load("media/start/profile_option.png").convert_alpha()
        self.USER_SLOT3_COORDS = (100, 600)

    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (100, 75))
        game_display.blit(self.USER_SLOT1, self.USER_SLOT1_COORDS)
        game_display.blit(self.USER_SLOT2, self.USER_SLOT2_COORDS)
        game_display.blit(self.USER_SLOT3, self.USER_SLOT3_COORDS)

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def step(self, stage):
        pass