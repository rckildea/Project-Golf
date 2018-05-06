import pygame
import GameObject
from gameobjects.objects import Button


class TitleScreen(GameObject.GameObject):
    def __init__(self):
        super().__init__(1)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/Title.png").convert()
        BUTTON_COLOR = (207, 255, 144, 10)
        FONT_COLOR = (255, 255, 255)
        self.course_select_button = Button.Button(self.DISPLAY_WIDTH / 4.5, self.DISPLAY_HEIGHT / 2, "generic_medium_button",
                                          "course select", BUTTON_COLOR, FONT_COLOR, True)
        self.create_character_button = Button.Button(self.DISPLAY_WIDTH / 1.8, self.DISPLAY_HEIGHT / 2, "generic_medium_button",
                                          "create character", BUTTON_COLOR, FONT_COLOR, True)
        self.load_profile_button = Button.Button(self.DISPLAY_WIDTH / 4.5, self.DISPLAY_HEIGHT / 1.5, "generic_medium_button",
                                          "load profile", BUTTON_COLOR, FONT_COLOR, True)
        self.quit_button = Button.Button(self.DISPLAY_WIDTH / 1.8, self.DISPLAY_HEIGHT / 1.5, "generic_medium_button",
                                          "quit", BUTTON_COLOR, FONT_COLOR, True)
        self.button_list = [self.course_select_button, self.create_character_button, self.load_profile_button, self.quit_button]

    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (0, 0))
        for button in self.button_list:
            button.draw(game_display)

    def handle_input(self, stage, events):
        for button in self.button_list:
            button.handle_input(stage, events)

        for event in events:
            pass

    def step(self, stage):
        if self.course_select_button.button_pressed:
            stage.game_engine.set_active_stage(stage.game_engine.stage_list[stage.game_engine.course_select_screen_index])
        if self.create_character_button.button_pressed:
            self.create_character_button.button_pressed = False
            stage.create_create_character_screen(stage.game_engine)
        if self.quit_button.button_pressed:
            pygame.quit()
            quit()

    def music(self):
        pygame.mixer.stop()
        pygame.mixer.music.load("media/start/theme.mp3")
        pygame.mixer.music.play(-1)