import pygame
from gameobjects.screens import CourseSelectScreen, CreateCharacterScreen, TitleScreen, PauseScreen, ScoreCard, TutorialScoreCard
import Course, Tutorial
from gameobjects.objects import Ball, Pin, SwingBar


class Stage(object):
    def __init__(self, game_engine):
        self.stage_objects = []
        self.game_engine = game_engine

        self.course = 0

    def add_object(self, game_obj):
        if len(self.stage_objects) == 0:
            self.stage_objects.append(game_obj)
        else:
            for i in range(0, len(self.stage_objects)):
                if game_obj.z_index <= self.stage_objects[i].z_index:
                    self.stage_objects.insert(i, game_obj)
                    break
                elif i == len(self.stage_objects) - 1:
                    self.stage_objects.append(game_obj)

    def draw(self, game_display):
        for game_object in self.stage_objects:
            if not game_object.hidden:
                game_object.draw(game_display)

    def handle_input(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        for game_object in self.stage_objects:
            if not game_object.ignore_input:
                game_object.handle_input(self, events)

    def step(self):
        for game_object in self.stage_objects:
            game_object.step(self)

    @staticmethod
    def create_title_screen(game_engine):
        title_screen = TitleScreen.TitleScreen()
        title_stage = Stage(game_engine)
        title_stage.add_object(title_screen)
        game_engine.add_stage(title_stage)
        game_engine.title_screen_index = game_engine.get_stage_index(title_stage)
        game_engine.set_active_stage(title_stage)
        Stage.create_course_select_screen(game_engine)

    @staticmethod
    def create_create_character_screen(game_engine):
        create_character_screen = CreateCharacterScreen.CreateCharacterScreen()
        create_character_stage = Stage(game_engine)
        create_character_stage.add_object(create_character_screen)
        game_engine.add_stage(create_character_stage)
        game_engine.set_active_stage(create_character_stage)

    @staticmethod
    def create_course_select_screen(game_engine):
        course_select = CourseSelectScreen.CourseSelectScreen()
        course_select_stage = Stage(game_engine)
        course_select_stage.add_object(course_select)
        game_engine.add_stage(course_select_stage)
        game_engine.course_select_screen_index = game_engine.get_stage_index(course_select_stage)

    def create_tutorial(self):
        self.course = Tutorial.Tutorial()
        self.golf_ball = Ball.Ball(self.course.hole_list[self.course.current_hole].tee_box_pos_x,
                                   self.course.hole_list[self.course.current_hole].tee_box_pos_y)
        self.swing_bar = SwingBar.SwingBar()
        self.pin = Pin.Pin()
        self.pause_screen = PauseScreen.PauseScreen()
        self.score_card = TutorialScoreCard.TutorialScoreCard(self.course)

        self.add_object(self.course.hole_list[self.course.current_hole])
        self.add_object(self.golf_ball)
        self.add_object(self.swing_bar)
        self.add_object(self.pin)
        self.add_object(self.pause_screen)
        self.add_object(self.score_card)

        self.game_engine.add_stage(self)
        self.game_engine.set_active_stage(self)

    def create_course(self, course_name):
        self.course = Course.Course(course_name)
        self.golf_ball = Ball.Ball(self.course.hole_list[self.course.current_hole].tee_box_pos_x,
                                   self.course.hole_list[self.course.current_hole].tee_box_pos_y)
        self.swing_bar = SwingBar.SwingBar()
        self.pin = Pin.Pin()
        self.pause_screen = PauseScreen.PauseScreen()
        self.score_card = ScoreCard.ScoreCard(self.course)

        self.add_object(self.course.hole_list[self.course.current_hole])
        self.add_object(self.golf_ball)
        self.add_object(self.swing_bar)
        self.add_object(self.pin)
        self.add_object(self.pause_screen)
        self.add_object(self.score_card)

        self.game_engine.add_stage(self)
        self.game_engine.set_active_stage(self)
