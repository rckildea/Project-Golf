import pygame
import GameObject


class Button(GameObject.GameObject):
    def __init__(self, x, y, image_name="JUNK", label_text="", color=(255, 255, 255), font_color=(0, 0, 0), stroke_text=False):
        super().__init__(10)
        self.button_image = pygame.image.load("media/start/{}.png".format(image_name)).convert_alpha()
        self.button_rect = self.button_image.get_rect(topleft=(x, y))
        self.COLOR = color
        self.button_image.fill(self.COLOR, special_flags=pygame.BLEND_MULT)
        self.x_position = x
        self.y_position = y
        self.coords = (self.x_position, self.y_position)
        self.button_pressed = False

        self.font_size = 24
        self.font = pygame.font.Font("media/start/big_noodle_titling.ttf", self.font_size)
        self.label_text = label_text
        self.label = self.font.render(self.label_text, 1, font_color)
        self.stroke_text = stroke_text
        if self.stroke_text:
            self.second_font = pygame.font.Font("media/start/big_noodle_titling.ttf", self.font_size)
            self.border = self.second_font.render(self.label_text, 1, (0, 0, 0))

    def draw(self, game_display):
        game_display.blit(self.button_image, (self.x_position, self.y_position))
        if self.stroke_text:
            self.blit_bold_text(game_display)
        game_display.blit(self.label, (self.button_rect.centerx - self.label.get_size()[0] / 2,
                                       self.button_rect.centery - self.label.get_size()[1]/ 2))
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
            if event.type == pygame.MOUSEBUTTONUP:
                self.button_pressed = False

    def blit_bold_text(self, game_display):
        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2 - 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2 - 2))
        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2 + 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2 + 2))
        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2 + 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2 - 2))
        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2 - 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2 + 2))

        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2 - 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2))
        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2 + 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2))

        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2 - 2))
        game_display.blit(self.border, (self.button_rect.centerx - self.label.get_size()[0] / 2,
                                        self.button_rect.centery - self.label.get_size()[1] / 2 + 2))
