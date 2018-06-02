import pygame
import GameObject
import Stage
from gameobjects.objects import Button


class TitleScreen(GameObject.GameObject):
    def __init__(self):
        super().__init__(1, True)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/Title.png").convert()
        BUTTON_COLOR = (207, 255, 144, 10)
        FONT_COLOR = (255, 255, 255)
        self.course_select_button = Button.Button(self.DISPLAY_WIDTH / 2.5, self.DISPLAY_HEIGHT / 1.75, "generic_medium_button",
                                          "course select", BUTTON_COLOR, FONT_COLOR, True)
        self.create_character_button = Button.Button(self.DISPLAY_WIDTH / 2.5, self.DISPLAY_HEIGHT / 1.75, "generic_medium_button",
                                          "create character", BUTTON_COLOR, FONT_COLOR, True)
        self.load_profile_button = Button.Button(self.DISPLAY_WIDTH / 2.5, self.DISPLAY_HEIGHT / 1.75, "generic_medium_button",
                                          "load profile", BUTTON_COLOR, FONT_COLOR, True)
        self.tutorial_button = Button.Button(self.DISPLAY_WIDTH / 2.5, self.DISPLAY_HEIGHT / 1.75, "generic_medium_button",
                                          "tutorial", BUTTON_COLOR, FONT_COLOR, True)
        self.quit_button = Button.Button(self.DISPLAY_WIDTH / 2.5, self.DISPLAY_HEIGHT / 1.75, "generic_medium_button",
                                          "quit", BUTTON_COLOR, FONT_COLOR, True)
        self.left_arrow = Button.Button(self.DISPLAY_WIDTH / 3.0, self.DISPLAY_HEIGHT / 1.71, "arrow_left",
                                          "", BUTTON_COLOR, FONT_COLOR, True)
        self.right_arrow = Button.Button(self.DISPLAY_WIDTH / 1.6, self.DISPLAY_HEIGHT / 1.71, "arrow_right",
                                          "", BUTTON_COLOR, FONT_COLOR, True)

        self.button_list = [self.course_select_button, self.create_character_button, self.load_profile_button, self.tutorial_button, self.quit_button]
        self.current_icon_index = 0 #TODO: Get rid of this, don't use index

    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (0, 0))
        for button in self.button_list:
            if not button.hidden:
                button.draw(game_display)
        self.left_arrow.draw(game_display)
        self.right_arrow.draw(game_display)

    def handle_input(self, stage, events):
        self.left_arrow.handle_input(stage, events)
        self.right_arrow.handle_input(stage, events)
        for button in self.button_list:
            if not button.ignore_input:
                button.handle_input(stage, events)
        for event in events:
            pass

    def step(self, stage):
        self.navigate_menu()
        if self.course_select_button.button_pressed:
            stage.game_engine.set_active_stage(stage.game_engine.stage_list[stage.game_engine.course_select_screen_index])
        if self.create_character_button.button_pressed:
            self.create_character_button.button_pressed = False
            stage.create_create_character_screen(stage.game_engine)
        if self.tutorial_button.button_pressed:
            hole_stage = Stage.Stage(stage.game_engine)
            hole_stage.create_tutorial()
        if self.quit_button.button_pressed:
            pygame.quit()
            quit()

    def navigate_menu(self):
        if self.left_arrow.button_pressed or self.right_arrow.button_pressed:
            if self.left_arrow.button_pressed:
                if self.current_icon_index > 0:
                    self.current_icon_index -= 1
                else:
                    self.current_icon_index = len(self.button_list) - 1
            if self.right_arrow.button_pressed:
                if self.current_icon_index < len(self.button_list) - 1:
                    self.current_icon_index += 1
                else:
                    self.current_icon_index = 0
            pygame.time.wait(150)
        for i in range(0, len(self.button_list)):
            if i == self.current_icon_index:
                self.button_list[i].set_active()
            else:
                self.button_list[i].set_inactive()

    def music(self):
        pygame.mixer.stop()
        pygame.mixer.music.load("media/start/theme.mp3")
        #pygame.mixer.music.play(-1)