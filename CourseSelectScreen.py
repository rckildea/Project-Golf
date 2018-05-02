import pygame
import GameObject
import CourseStage


class CourseSelectScreen(GameObject.GameObject):
    def __init__(self):
        super().__init__(1)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/courseselect.png").convert()
        self.SPRING_MEADOWS_BUTTON = pygame.image.load("media/start/springmeadows.png").convert()
        self.SPRING_MEADOWS_BUTTON_RECT = self.SPRING_MEADOWS_BUTTON.get_rect()
        self.SPRING_MEADOWS_BUTTON2 = pygame.image.load("media/start/springmeadows2.png").convert()
        self.SPRING_MEADOWS_BUTTON3 = pygame.image.load("media/start/springmeadows2.png").convert()

    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (0, 0))
        game_display.blit(self.SPRING_MEADOWS_BUTTON, (self.DISPLAY_WIDTH / 4 - 64, self.DISPLAY_HEIGHT / 3))
        game_display.blit(self.SPRING_MEADOWS_BUTTON2, (self.DISPLAY_WIDTH / 2 - 64, self.DISPLAY_HEIGHT / 3))
        game_display.blit(self.SPRING_MEADOWS_BUTTON3, (self.DISPLAY_WIDTH * 0.75 - 64, self.DISPLAY_HEIGHT / 3))
        self.SPRING_MEADOWS_BUTTON_RECT = self.SPRING_MEADOWS_BUTTON.get_rect(topleft=(self.DISPLAY_WIDTH / 4 - 64, self.DISPLAY_HEIGHT / 3))

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if self.SPRING_MEADOWS_BUTTON_RECT.collidepoint(x, y):
                    CourseStage.CourseStage(stage.game_engine, "Spring Meadows")