import pygame
import GameObject


class Pin(GameObject.GameObject):
    def __init__(self):
        super().__init__(5)
        self.pin_img = pygame.image.load("media/game/hole.png").convert_alpha()
        self.flag_img = pygame.image.load("media/game/flag.png").convert_alpha()
        self.pin_pos_x = 700
        self.pin_pos_y = 70
        self.pin_rect = self.pin_img.get_rect()
        self.update_rect()

        self.flag_pos_x = self.pin_pos_x + 4
        self.flag_pos_y = self.pin_pos_y - 24

    def draw(self, game_display):
        game_display.blit(self.pin_img, (self.pin_pos_x, self.pin_pos_y))
        game_display.blit(self.flag_img, (self.flag_pos_x, self.flag_pos_y))

    def handle_input(self, stage, events):
        pass

    def step(self, stage):
        pass

    def update_rect(self):
        self.pin_rect.x = self.pin_pos_x
        self.pin_rect.y = self.pin_pos_y
