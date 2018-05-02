import Hole
import pygame


class Course:
    def __init__(self, name):
        self.course_name = name
        self.hole_list = Course.populate_course(self)
        self.current_hole = 0

    # Create a hole for every hole in a course - 18 per course
    def populate_course(self):
        hole_list = []
        if self.course_name == "Spring Meadows":
            for i in range(0, 17):
                hole_list.append(Hole.Hole(i, self.course_name))
        return hole_list

    def start_music(self):
        pygame.mixer.music.load("media/courses/{course}/theme.mp3".format(course=self.course_name))
        pygame.mixer.stop()
        pygame.mixer.music.play(-1)
