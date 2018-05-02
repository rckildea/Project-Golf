import pygame
import GameObject


class CreateCharacterScreen(GameObject.GameObject):
    def __init__(self):
        super().__init__(1)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/create_character_screen.png").convert()
        self.BACKGROUND_RECT = self.BACKGROUND_IMAGE.get_rect()
        self.strength_bar = pygame.image.load("media/start/stat_bar.png").convert_alpha()
        self.control_bar = pygame.image.load("media/start/stat_bar.png").convert_alpha()
        self.stat_bar_x = self.BACKGROUND_RECT.centerx - self.strength_bar.get_size()[0] / 2
        self.strength_bar_y = self.DISPLAY_HEIGHT / 2.5
        self.control_bar_y = self.DISPLAY_HEIGHT / 2
        self.strength_bar.fill((255, 144, 144, 43), special_flags=pygame.BLEND_MULT)
        self.control_bar.fill((255, 212, 144, 9), special_flags=pygame.BLEND_MULT)

        self.point_image = pygame.image.load("media/start/stat_point.png").convert_alpha()

        self.strength = 3 # DELETE LATER
        self.control = 4 # DELETE LATER

        self.strength_points = []
        self.control_points = []
        self.fill_points()


    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (0, 0))
        game_display.blit(self.strength_bar, (self.stat_bar_x, self.strength_bar_y))
        game_display.blit(self.control_bar, (self.stat_bar_x, self.control_bar_y))
        self.display_stat_points(game_display)

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.strength += 1
                    print("{} in loop".format(self.strength))
                if event.key == pygame.K_o:
                    self.strength -= 1
                self.fill_points()

    def step(self, stage):
        pass

    def fill_points(self):
        # TESTING
        self.strength_points = []
        self.control_points = []

        current_stat_point = pygame.image.load("media/start/stat_point.png").convert_alpha()
        current_stat_point.fill((255, 144, 144, 43), special_flags=pygame.BLEND_MULT)
        for i in range(1, self.strength + 1):
            print(self.strength)
            self.strength_points.append(current_stat_point)
        for i in range(12, self.strength, -1):
            self.strength_points.append(self.point_image)
        current_stat_point = pygame.image.load("media/start/stat_point.png").convert_alpha()
        current_stat_point.fill((255, 212, 144, 9), special_flags=pygame.BLEND_MULT)
        for i in range(1, self.control + 1):
            self.control_points.append(current_stat_point)
        for i in range(12, self.control, -1):
            self.control_points.append(self.point_image)

    def display_stat_points(self, game_display):
        offset = 18
        for point in self.strength_points:
            game_display.blit(point, (self.stat_bar_x + offset, self.strength_bar_y + 15))
            offset += 30
        offset = 18
        for point in self.control_points:
            game_display.blit(point, (self.stat_bar_x + offset, self.control_bar_y + 15))
            offset += 30
