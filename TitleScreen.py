import pygame
import Button
import GameObject


class TitleScreen(GameObject.GameObject):
    def __init__(self):
        super().__init__(1)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/Title.png").convert()
        self.start_button = Button.Button(self.DISPLAY_WIDTH / 2.5, self.DISPLAY_HEIGHT / 1.5)
        self.start_button.button_image = pygame.image.load("media/start/startbutton.png").convert()

    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (0, 0))
        self.start_button.draw(game_display)

    def handle_input(self, stage, events):
        self.start_button.handle_input(stage, events)
        if self.start_button.button_pressed:
            self.start_button.button_pressed = False
            stage.create_create_character_screen()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def music(self):
        pygame.mixer.stop()
        pygame.mixer.music.load("media/start/theme.mp3")
        pygame.mixer.music.play(-1)