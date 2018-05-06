import pygame
import GameObject
from gameobjects.objects import Button


class PauseScreen(GameObject.GameObject):
    def __init__(self):
        super().__init__(8)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/pausescreen.png").convert_alpha()
        self.resume_button = Button.Button(self.DISPLAY_WIDTH / 2.6, self.DISPLAY_HEIGHT / 2)
        self.resume_button.button_image = pygame.image.load("media/start/resumebutton.png").convert_alpha()
        self.set_inactive()

    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (self.DISPLAY_WIDTH / 20, self.DISPLAY_HEIGHT / 10))
        self.resume_button.draw(game_display)

    def handle_input(self, stage, events):
        self.resume_button.handle_input(stage, events)
        if self.resume_button.button_pressed:
            self.set_inactive()
            self.resume_button.button_pressed = False
            stage.golf_ball.ignore_input = False
            stage.swing_bar.ignore_input = False

    def step(self, stage):
        pass