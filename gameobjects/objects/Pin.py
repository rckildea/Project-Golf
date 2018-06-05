import pygame
import GameObject
import random


class Pin(GameObject.GameObject):
    def __init__(self, course):
        super().__init__(5)
        self.course = course
        self.pin_img = pygame.image.load("media/game/hole.png").convert_alpha()
        self.flag_img = pygame.image.load("media/game/flag.png").convert_alpha()
        self.pin_coords = (0, 0)
        self.get_coords()
        self.pin_rect = self.pin_img.get_rect()
        self.update_rect()

        self.flag_coords = (self.pin_coords[0] + 4, self.pin_coords[1] - 24)

    def draw(self, game_display):
        game_display.blit(self.pin_img, self.pin_coords)
        game_display.blit(self.flag_img, self.flag_coords)

    def handle_input(self, stage, events):
        pass

    def step(self, stage):
        pass

    def update_rect(self):
        self.pin_rect.x = self.pin_coords[0]
        self.pin_rect.y = self.pin_coords[1]

    def get_coords(self):
        file = "media/courses/{course}/properties/pin_locations.txt".format(course=self.course.course_name)
        seed_num = random.randint(0, 2)
        reader = open(file, 'r')
        lines = reader.readlines()
        coords = lines[self.course.current_hole]
        coords = coords.split(',')
        self.pin_coords = (int(coords[2*seed_num]), int(coords[2*seed_num + 1]))
        reader.close()
