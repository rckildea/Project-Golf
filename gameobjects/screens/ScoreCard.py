import pygame
import GameObject
from gameobjects.objects import Button

class ScoreCard(GameObject.GameObject):
    def __init__(self, course):
        super().__init__(20)
        self.background_image = pygame.image.load("media/start/blankbackground.png").convert_alpha()
        self.front_9_image = pygame.image.load("media/start/scorecardfront.png").convert_alpha()
        self.back_9_image = pygame.image.load("media/start/scorecardback.png").convert_alpha()
        self.character_front_9 = pygame.image.load("media/start/scorecardplayer.png").convert_alpha()
        self.character_back_9 = pygame.image.load("media/start/scorecardplayer.png").convert_alpha()
        self.course = course

        self.coords = (100, 220)
        self.top_line_x = self.coords[0] + 275
        self.top_line_y = self.coords[1] + 4
        self.bottom_line_x = self.coords[0] + 183
        self.bottom_line_y = self.coords[1] + 65
        self.character_coords = (self.coords[0], self.coords[1] + 91)
        self.character_line_x = self.coords[0] + 7
        self.character_line_y = self.coords[1] + 94

        self.close_button = Button.Button(self.coords[0],
                                               self.coords[1] + self.front_9_image.get_size()[1] + 30,
                                               "generic_small_button", "close")
        self.swap_sides_button = Button.Button(self.coords[0] + self.front_9_image.get_size()[0] - 80,
                                               self.coords[1] + self.front_9_image.get_size()[1] + 30,
                                               "generic_small_button", "flip")

        self.front_active = True

        self.user_stroke_list = []

        self.user_score = 0
        self.user_front_9_strokes = 0
        self.user_back_9_strokes = 0
        self.user_total_strokes = 0
        self.user_name = ""


        self.set_inactive()

    def draw(self, game_display):
        self.draw_card(game_display)
        self.close_button.draw(game_display)
        self.swap_sides_button.draw(game_display)

        game_display.blit(self.character_front_9, self.character_coords)
        self.draw_user_score(game_display)

    def handle_input(self, stage, events):
        self.close_button.handle_input(stage, events)
        self.swap_sides_button.handle_input(stage, events)

    def step(self, stage):
        self.user_stroke_list = stage.game_engine.character.stroke_list
        self.user_name = stage.game_engine.character.name
        if self.close_button.button_pressed:
            self.close_button.button_pressed = False
            stage.golf_ball.ignore_input = False
            stage.swing_bar.ignore_input = False
            self.set_inactive()
        if self.swap_sides_button.button_pressed:
            self.front_active = not self.front_active
            self.swap_sides_button.button_pressed = False
        self.calculate_score()

    def draw_card(self, game_display):
        game_display.blit(self.background_image, (100, 220))
        game_display.blit(self.course.course_icon, self.coords)
        if self.front_active:
            game_display.blit(self.front_9_image, self.coords)
        else:
            game_display.blit(self.back_9_image, self.coords)
        hole_text = self.FONT_24.render("{}".format(self.course.course_name), 1, (0, 0, 0))
        game_display.blit(hole_text, (self.top_line_x, self.top_line_y))

        self.bottom_line_x = self.coords[0] + 183
        self.bottom_line_y = self.coords[1] + 65
        start = 0 if self.front_active else 9
        end = 9 if self.front_active else 18
        for i in range (start, end):
            hole_text = self.FONT_24.render("{}".format(self.course.hole_list[i].par), 1, (0, 0, 0))
            game_display.blit(hole_text, (self.bottom_line_x, self.bottom_line_y))
            self.bottom_line_x += 30
        self.bottom_line_x -= 3
        hole_text = self.FONT_24.render("{}".format(self.course.front_9_strokes if self.front_active else self.course.back_9_strokes), 1, (0, 0, 0))
        game_display.blit(hole_text, (self.bottom_line_x, self.bottom_line_y))
        self.bottom_line_x += 30
        hole_text = self.FONT_24.render("{}".format(self.course.strokes), 1, (0, 0, 0))
        game_display.blit(hole_text, (self.bottom_line_x, self.bottom_line_y))

    def draw_user_score(self, game_display):
        self.character_line_x = self.coords[0] + 7
        self.character_line_y = self.coords[1] + 94

        score_text = self.FONT_24.render("{}".format(self.user_name), 1, (0, 0, 0))
        game_display.blit(score_text, (self.character_line_x, self.character_line_y))

        self.character_line_x += 176

        start = 0 if self.front_active else 9
        end = 9 if self.front_active else 18

        for i in range(start, end):
            score_text = self.FONT_24.render("{}".format(self.user_stroke_list[i]), 1, (0, 0, 0))
            if self.user_stroke_list[i] != 0:
                game_display.blit(score_text, (self.character_line_x, self.character_line_y))
            self.character_line_x += 30

        self.character_line_x += 2

        if self.front_active:
            score_text = self.FONT_24.render("{}".format(self.user_front_9_strokes), 1, (0, 0, 0))
        else:
            score_text = self.FONT_24.render("{}".format(self.user_back_9_strokes), 1, (0, 0, 0))
        game_display.blit(score_text, (self.character_line_x, self.character_line_y))

        self.character_line_x += 30

        score_text = self.FONT_24.render("{}".format(self.user_total_strokes), 1, (0, 0, 0))
        game_display.blit(score_text, (self.character_line_x, self.character_line_y))

        self.character_line_x += 60

        score_text = self.FONT_24.render("{}".format(self.user_score), 1, (0, 0, 0))
        game_display.blit(score_text, (self.character_line_x, self.character_line_y))

    def calculate_score(self):
        user_sum = 0
        par = 0
        self.user_front_9_strokes = sum(self.user_stroke_list[0:9])
        self.user_back_9_strokes = sum(self.user_stroke_list[9:18])

        for i in range(0, 18):
            if not self.user_stroke_list[i] == 0:
                user_sum += self.user_stroke_list[i]
                par += self.course.hole_list[i].par

        self.user_score = user_sum - par
        self.user_total_strokes = self.user_front_9_strokes + self.user_back_9_strokes
