import pygame
from gameobjects.screens import PauseScreen, ScoreCard, TutorialScoreCard
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