import pygame
import GameObject
import Status


class CreateCharacterScreen(GameObject.GameObject):
    def __init__(self, stage):
        super().__init__(1)
        self.BACKGROUND_IMAGE = pygame.image.load("media/start/create_character_screen.png").convert()
        self.BACKGROUND_RECT = self.BACKGROUND_IMAGE.get_rect()
        self.TITLE = self.FONT_64.render("Character Creation", 1, (0, 0, 0))

        self.STRENGTH_COLOR = (255, 144, 144, 43)
        self.CONTROL_COLOR = (255, 212, 144, 9)
        self.UNKNOWN1_COLOR = (80, 255, 120, 67)
        self.UNKNOWN2_COLOR = (80, 84, 255, 41)
        self.UNKNOWN3_COLOR = (230, 47, 250, 30)

        self.INITIAL_Y_POS = self.DISPLAY_HEIGHT / 4

        self.strength = Status.Status("Strength", self.STRENGTH_COLOR, self.INITIAL_Y_POS)
        self.control = Status.Status("Control", self.CONTROL_COLOR, self.INITIAL_Y_POS + 60)
        self.unknown1 = Status.Status("Unknown1", self.UNKNOWN1_COLOR, self.INITIAL_Y_POS + 120)
        self.unknown2 = Status.Status("Unknown2", self.UNKNOWN2_COLOR, self.INITIAL_Y_POS + 180)
        self.unknown3 = Status.Status("Unknown3", self.UNKNOWN3_COLOR, self.INITIAL_Y_POS + 240)

        self.status_list = [self.strength, self.control, self.unknown1, self.unknown2, self.unknown3]

        self.points_text = self.FONT_20.render("Status points: {points}".format(points=0), 1, (0, 0, 0))


    def draw(self, game_display):
        game_display.blit(self.BACKGROUND_IMAGE, (0, 0))
        game_display.blit(self.TITLE, (self.BACKGROUND_RECT.centerx - self.TITLE.get_size()[0] / 2, 30))
        game_display.blit(self.points_text, (self.strength.status_bar_rect.centerx - self.points_text.get_size()[0] / 2, self.INITIAL_Y_POS - 20))
        for status in self.status_list:
            status.draw(game_display)

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for status in self.status_list:
            status.handle_input(stage, events)

    def step(self, stage):
        self.points_text = self.FONT_20.render("Status points: {points}".format(points=stage.character.status_points), 1, (0, 0, 0))
        for status in self.status_list:
            status.step(stage)