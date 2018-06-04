import pygame
import Stage, CourseStage, TutorialStage
from gameobjects.screens import CourseSelectScreen, CreateCharacterScreen, TitleScreen


class StageFactory():
    def __init__(self):
        pass

    @staticmethod
    def create_title_screen(game_engine):
        title_screen = TitleScreen.TitleScreen()
        title_stage = Stage.Stage(game_engine)
        title_stage.add_object(title_screen)
        game_engine.add_stage(title_stage)
        game_engine.title_screen_index = game_engine.get_stage_index(title_stage)
        game_engine.set_active_stage(title_stage)
        StageFactory.create_course_select_screen(game_engine)

    @staticmethod
    def create_create_character_screen(game_engine):
        create_character_screen = CreateCharacterScreen.CreateCharacterScreen()
        create_character_stage = Stage.Stage(game_engine)
        create_character_stage.add_object(create_character_screen)
        game_engine.add_stage(create_character_stage)
        game_engine.set_active_stage(create_character_stage)

    @staticmethod
    def create_course_select_screen(game_engine):
        course_select = CourseSelectScreen.CourseSelectScreen()
        course_select_stage = Stage.Stage(game_engine)
        course_select_stage.add_object(course_select)
        game_engine.add_stage(course_select_stage)
        game_engine.course_select_screen_index = game_engine.get_stage_index(course_select_stage)

    @staticmethod
    def create_course(game_engine, course_name):
        course_stage = CourseStage.CourseStage(game_engine, course_name)
        game_engine.add_stage(course_stage)
        game_engine.set_active_stage(course_stage)

    @staticmethod
    def create_tutorial(game_engine):
        tutorial_stage = TutorialStage.TutorialStage(game_engine)
        game_engine.add_stage(tutorial_stage)
        game_engine.set_active_stage(tutorial_stage)