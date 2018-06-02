from gameobjects.objects import TutorialHole
import pygame


class Tutorial:
    def __init__(self):
        self.course_name = "Tutorial"
        self.hole_list = []
        self.hole_list.append(TutorialHole.TutorialHole(1, self.course_name))
        self.current_hole = 0
        self.course_icon = pygame.image.load("media/courses/{course}/icon.png".format(course=self.course_name))
        self.score_card_icon = pygame.transform.scale(self.course_icon, (64, 64))
        self.front_9_strokes = self.get_strokes(0)
        self.strokes = self.front_9_strokes

    def get_strokes(self, start):
        return 4