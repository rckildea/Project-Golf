import pygame
import GameObject


class Button(GameObject.GameObject):
    def __init__(self, x, y):
        super().__init__(10)
        self.button_image = pygame.image.load("media/start/JUNK.png").convert()
        self.button_rect = self.button_image.get_rect(topleft=(x, y))
        self.x_position = x
        self.y_position = y
        self.button_pressed = False

    def draw(self, game_display):
        game_display.blit(self.button_image, (self.x_position, self.y_position))
        self.button_rect = self.button_image.get_rect(topleft=(self.x_position, self.y_position))

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.button_rect.collidepoint(x, y):
                    self.button_pressed = True
