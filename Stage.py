import pygame
import Engine
import TitleScreen
import CourseSelectScreen
import Course
import Ball
import SwingBar
import Pin


class Stage(object):

    def __init__(self, game_engine):
        self.stage_objects = []

        self.game_engine = game_engine

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
        for game_object in self.stage_objects:
            if not game_object.hidden:
                game_object.handle_input(self, events)

    def step(self):
        for game_object in self.stage_objects:
            game_object.step(self)

    def create_title_screen(self):
        title_screen = TitleScreen.TitleScreen()
        title_stage = Stage(self.game_engine)
        title_stage.add_object(title_screen)
        self.game_engine.add_stage(title_stage)
        self.game_engine.set_active_stage(title_stage)

    def create_course_select_screen(self):
        course_select = CourseSelectScreen.CourseSelectScreen()
        course_select_stage = Stage(self.game_engine)
        course_select_stage.add_object(course_select)
        self.game_engine.add_stage(course_select_stage)
        self.game_engine.set_active_stage(course_select_stage)
