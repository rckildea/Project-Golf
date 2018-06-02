import pygame
import GameObject


class TutorialHole(GameObject.GameObject):
    def __init__(self, number, course):
        super().__init__(1, True)
        self.hole_number = number
        self.course_name = course
        self.hole_background = pygame.image.load(
            "media/courses/{course}/hole{num}/hole{num}.png".format(course=self.course_name,
                                                                    num=self.hole_number)).convert()
        self.arrow_keys = pygame.image.load("media/tutorial/arrow_keys.png".format()).convert_alpha()
        self.space_key = pygame.image.load("media/tutorial/space_bar.png".format()).convert_alpha()
        self.p_key = pygame.image.load("media/tutorial/p_key.png".format()).convert_alpha()
        self.s_key = pygame.image.load("media/tutorial/s_key.png".format()).convert_alpha()
        self.par = 4
        self.tee_box_pos_x = 295
        self.tee_box_pos_y = 442

        self.font = pygame.font.Font("media/start/big_noodle_titling.ttf", 20)
        self.arrow_instr = self.font.render("Arrow Keys: Adjust direction", 1, (255, 255, 255))
        self.space_instr1 = self.font.render("Space Bar:", 1, (255, 255, 255))
        self.space_instr2 = self.font.render("Press to begin swing", 1, (255, 255, 255))
        self.space_instr3 = self.font.render("Press again to set power", 1, (255, 255, 255))
        self.space_instr4 = self.font.render("Press a third time to set accuracy", 1, (255, 255, 255))
        self.p_instr = self.font.render("P: Opens pause menu", 1, (255, 255, 255))
        self.s_instr = self.font.render("S: View scorecard", 1, (255, 255, 255))

        self.power_text = self.font.render("POWER:", 1, (255, 255, 255))
        self.previous_power = 0
        self.accuracy_text = self.font.render("ACCURACY:", 1, (255, 255, 255))

    def draw(self, game_display):
        game_display.blit(self.hole_background, (0, 0))
        game_display.blit(self.arrow_keys, (10, 20))
        game_display.blit(self.arrow_instr, (10, 90))
        game_display.blit(self.space_key, (10, 120))
        game_display.blit(self.space_instr1, (10, 155))
        game_display.blit(self.space_instr2, (10, 175))
        game_display.blit(self.space_instr3, (10, 195))
        game_display.blit(self.space_instr4, (10, 215))
        game_display.blit(self.p_key, (10, 245))
        game_display.blit(self.p_instr, (10, 280))
        game_display.blit(self.s_key, (10, 315))
        game_display.blit(self.s_instr, (10, 350))
        game_display.blit(self.power_text, (10, 390))
        game_display.blit(self.accuracy_text, (10, 410))

    def handle_input(self, stage, events):
        if stage.swing_bar.power_num != 0:
            self.previous_power = stage.swing_bar.power_num
        self.power_text = self.font.render("POWER: {}".format(self.previous_power), 1, (255, 255, 255))
        self.accuracy_text = self.font.render("Accuracy: {}".format(stage.swing_bar.accuracy), 1, (255, 255, 255))
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    self.display_pause_screen(stage)
                if event.key == pygame.K_s:
                    self.display_score_card(stage)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

    def display_pause_screen(self, stage):
        stage.pause_screen.set_active()
        stage.golf_ball.ignore_input = True
        stage.swing_bar.ignore_input = True

    def display_score_card(self, stage):
        stage.score_card.set_active()
        stage.golf_ball.ignore_input = True
        stage.swing_bar.ignore_input = True

    def music(self):
        pygame.mixer.stop()
        pygame.mixer.music.load("media/courses/{course}/theme.mp3".format(course=self.course_name))
        #pygame.mixer.music.play(-1)