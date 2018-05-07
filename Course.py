from gameobjects.objects import Hole
import pygame


class Course:
    def __init__(self, name):
        self.course_name = name
        self.hole_list = Course.populate_course(self)
        self.current_hole = 0
        self.course_icon = pygame.image.load("media/courses/{course}/icon.png".format(course=self.course_name))
        self.front_9_strokes = self.get_strokes(0)
        self.back_9_strokes = self.get_strokes(9)
        self.strokes = self.front_9_strokes + self.back_9_strokes

    # Create a hole for every hole in a course - 18 per course
    def populate_course(self):
        hole_list = []
        if self.course_name == "Spring Meadows":
            for i in range(0, 18):
                hole_list.append(Hole.Hole(i+1, self.course_name))

        return hole_list

    def get_strokes(self, start):
        end = start+9
        sum = 0
        for i in range(start, end):
            sum += self.hole_list[i].get_par()
        return sum