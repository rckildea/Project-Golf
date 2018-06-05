import pygame
import GameObject


class Hole(GameObject.GameObject):
    def __init__(self, number, course):
        super().__init__(1, True)
        self.hole_number = number
        self.course_name = course
        self.hole_background = pygame.image.load(
            "media/courses/{course}/hole{num}/hole{num}.png".format(course=self.course_name,
                                                                    num=self.hole_number)).convert()
        self.par = Hole.get_par(self)
        self.tee_box_pos_x = 0
        self.tee_box_pos_y = 0
        Hole.get_tee_box(self)

        self.hole_score = 0

    def draw(self, game_display):
        game_display.blit(self.hole_background, (0, 0))
        if not self.hole_score == 0:
            stroke_text = self.FONT_128.render("{score}".format(score=self.get_user_score_name()), 1, (255, 255, 255))
            game_display.blit(stroke_text, ((self.DISPLAY_WIDTH - stroke_text.get_size()[0]) / 2, (self.DISPLAY_HEIGHT - stroke_text.get_size()[1]) / 2))

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.display_pause_screen(stage)
                if event.key == pygame.K_s:
                    self.display_score_card(stage)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def get_par(self):
        if self.course_name == "Spring Meadows":
            par_list = [0, 4, 4, 3, 5, 4, 4, 3, 4, 5, 4, 4, 5, 4, 3, 4, 5, 3, 4]
            return par_list[self.hole_number]
        return 0

    def get_tee_box(self):
        file = "media/courses/{course}/properties/tee_box.txt".format(course=self.course_name)
        reader = open(file, 'r')
        lines = reader.readlines()
        coords = lines[self.hole_number-1]
        coords = coords.split(',')
        self.tee_box_pos_x = coords[0]
        self.tee_box_pos_y = coords[1]
        reader.close()

    def display_pause_screen(self, stage):
        stage.pause_screen.set_active()
        stage.golf_ball.ignore_input = True
        stage.swing_bar.ignore_input = True

    def display_score_card(self, stage):
        stage.score_card.set_active()
        stage.golf_ball.ignore_input = True
        stage.swing_bar.ignore_input = True

    def display_score_hole_out(self, stage):
        self.hole_score = stage.game_engine.character.current_stroke

    def get_user_score_name(self):
        user_score = self.hole_score - self.par
        if self.par + user_score == 1:
            return "Hole in One!"
        if self.par > 4 and user_score == -3:
            return "Albatross!"
        if self.par > 3 and user_score == -2:
            return "Eagle!"
        if user_score == -1:
            return "Birdie!"
        if user_score == 0:
            return "Par"
        if user_score == 1:
            return "Bogey"
        if user_score == 2:
            return "Double Bogey"
        if user_score == 3:
            return "Triple Bogey"
        else:
            return "+" + str(user_score)

    def music(self):
        pygame.mixer.stop()
        pygame.mixer.music.load("media/courses/{course}/theme.mp3".format(course=self.course_name))
        #pygame.mixer.music.play(-1)