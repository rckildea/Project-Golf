import pygame
import GameObject
import Button

class Status(GameObject.GameObject):
    def __init__(self, name, color, y):
        super().__init__(6)
        self.name = name
        self.color = color
        self.points = 0
        self.status_bar = pygame.image.load("media/start/stat_bar.png").convert_alpha()
        self.status_bar.fill(self.color, special_flags=pygame.BLEND_MULT)

        self.status_bar_x = 430 - self.status_bar.get_size()[0] / 2 + 50 # TODO: Get rid of magic numbers
        self.status_bar_y = y
        self.status_bar_rect = self.status_bar.get_rect(topleft=(self.status_bar_x, self.status_bar_y))

        self.status_bar_label = pygame.image.load("media/start/{name}_text.png".format(name=self.name)).convert_alpha()
        self.status_bar_label.fill(self.color, special_flags=pygame.BLEND_MULT)

        self.status_minus_button = Button.Button(self.status_bar_x - 35, self.status_bar_y + 20)
        self.status_plus_button = Button.Button(self.status_bar_x + self.status_bar.get_size()[0] + 5,
                                                  self.status_bar_y + 10)
        self.status_minus_button.button_image = pygame.image.load("media/start/stat_bar_minus.png").convert_alpha()
        self.status_plus_button.button_image = pygame.image.load("media/start/stat_bar_plus.png").convert_alpha()
        self.status_minus_button.button_image.fill(self.color, special_flags=pygame.BLEND_MULT)
        self.status_plus_button.button_image.fill(self.color, special_flags=pygame.BLEND_MULT)

        self.status_val_text = self.FONT_20.render("{}".format(self.points), 1, (0, 0, 0))

        self.point_image = pygame.image.load("media/start/stat_point.png").convert_alpha()
        self.point_image_list = []

    def draw(self, game_display):
        game_display.blit(self.status_bar, (self.status_bar_x, self.status_bar_y))
        game_display.blit(self.status_val_text, (self.status_bar_x + 360, self.status_bar_y + 14))
        game_display.blit(self.status_bar_label, (self.status_bar_x - 210, self.status_bar_y + 5))
        self.status_minus_button.draw(game_display)
        self.status_plus_button.draw(game_display)
        self.display_status_points(game_display)

    def handle_input(self, stage, events):
        self.status_minus_button.handle_input(stage, events)
        self.status_plus_button.handle_input(stage, events)

    def step(self, stage):
        self.fill_points()
        self.get_status_point_update(stage)
        self.status_val_text = self.FONT_20.render("{}".format(self.points), 1, (0, 0, 0))

    def fill_points(self):
        self.point_image_list = []
        current_stat_point = pygame.image.load("media/start/stat_point.png").convert_alpha()
        current_stat_point.fill(self.color, special_flags=pygame.BLEND_MULT)
        for i in range(1, self.points + 1):
            self.point_image_list.append(current_stat_point)
        for i in range(40, self.points, -1):
            self.point_image_list.append(self.point_image)

    def display_status_points(self, game_display):
        offset = 18
        for point in self.point_image_list:
            game_display.blit(point, (self.status_bar_x + offset, self.status_bar_y + 15))
            offset += 8

    def get_status_point_update(self, stage):
        if self.status_minus_button.button_pressed and not self.points == 0:
            self.points -= 1
            stage.character.status_points += 1

        if self.status_plus_button.button_pressed and not stage.character.status_points == 0 and not self.points >= 40:
            self.points += 1
            stage.character.status_points -= 1

        pygame.time.wait(15)
        #self.status_minus_button.button_pressed = False
        #self.status_plus_button.button_pressed = False