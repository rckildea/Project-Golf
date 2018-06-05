from gameobjects.objects import Hole
import pygame
import StageFactory


class Course:
    def __init__(self, name):
        self.course_name = name
        self.hole_list = Course.populate_course(self)
        self.current_hole = 0
        self.course_icon = pygame.image.load("media/courses/{course}/icon.png".format(course=self.course_name))
        self.score_card_icon = pygame.transform.scale(self.course_icon, (64, 64))
        self.front_9_strokes = self.get_strokes(0)
        self.back_9_strokes = self.get_strokes(9)
        self.strokes = self.front_9_strokes + self.back_9_strokes

    # Create a hole for every hole in a course - 18 per course
    def populate_course(self):
        hole_list = []
        for i in range(0, 18):
            hole_list.append(Hole.Hole(i+1, self.course_name)) # Hole numbers offset by 1 of their actual index

        return hole_list

    def get_current_hole(self):
        return self.hole_list[self.current_hole]

    def get_strokes(self, start):
        # Returns only strokes for front nine or back nine
        end = start+9
        total = 0
        for i in range(start, end):
            total += self.hole_list[i].get_par()
        return total

    def next_hole(self, stage):
        if self.current_hole < 18:
            self.current_hole += 1
            StageFactory.StageFactory.create_hole(stage.game_engine, self)