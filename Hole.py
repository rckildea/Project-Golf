import pygame
import GameObject


class Hole(GameObject.GameObject):
    def __init__(self, number, course):
        super().__init__(1)
        self.hole_number = number + 1
        self.course_name = course
        self.hole_background = pygame.image.load(
            "media/courses/{course}/hole{num}/hole{num}.png".format(course=self.course_name,
                                                                    num=self.hole_number)).convert()
        self.par = Hole.get_par(self)
        self.tee_box_pos_x = 0
        self.tee_box_pos_y = 0
        Hole.get_tee_box(self)

    def draw(self, game_display):
        game_display.blit(self.hole_background, (0, 0))

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    stage.pause_screen.hidden = False
                    print("Here")
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def get_par(self):
        if self.course_name == "Spring Meadows":
            par_list = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
            return par_list[self.hole_number]
        return 0

    def get_tee_box(self):
        file = "media/courses/Spring Meadows/properties/tee_box.txt".format(course=self.course_name)
        reader = open(file, 'r')
        lines = reader.readlines()
        coords = lines[self.hole_number-1]
        coords = coords.split(',')
        self.tee_box_pos_x = coords[0]
        self.tee_box_pos_y = coords[1]
        reader.close()