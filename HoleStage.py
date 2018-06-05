import Stage
from gameobjects.screens import PauseScreen, ScoreCard
import Course
from gameobjects.objects import Ball, Pin, SwingBar


class HoleStage(Stage.Stage):
    def __init__(self, game_engine, course):
        super().__init__(game_engine)
        self.course = course
        self.hole = self.course.current_hole
        self.golf_ball = Ball.Ball(self.course.hole_list[self.course.current_hole].tee_box_pos_x,
                                   self.course.hole_list[self.course.current_hole].tee_box_pos_y)
        self.swing_bar = SwingBar.SwingBar()
        self.pin = Pin.Pin(course)
        self.pause_screen = PauseScreen.PauseScreen()
        self.score_card = ScoreCard.ScoreCard(self.course)

        self.add_object(self.course.hole_list[self.course.current_hole])
        self.add_object(self.golf_ball)
        self.add_object(self.swing_bar)
        self.add_object(self.pin)
        self.add_object(self.pause_screen)
        self.add_object(self.score_card)

        self.game_engine.add_stage(self)
        self.game_engine.set_active_stage(self)