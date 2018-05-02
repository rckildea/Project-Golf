import Stage
import Course
import Ball
import SwingBar
import Pin
import PauseScreen


class CourseStage(Stage.Stage):
    def __init__(self, game_engine, course_name):
        super().__init__(game_engine)
        self.course = Course.Course(course_name)
        self.golf_ball = Ball.Ball(self.course.hole_list[self.course.current_hole].tee_box_pos_x,
                                   self.course.hole_list[self.course.current_hole].tee_box_pos_y)
        self.swing_bar = SwingBar.SwingBar()
        self.pin = Pin.Pin()
        self.pause_screen = PauseScreen.PauseScreen()

        self.add_object(self.course.hole_list[self.course.current_hole])
        self.add_object(self.golf_ball)
        self.add_object(self.swing_bar)
        self.add_object(self.pin)
        self.add_object((self.pause_screen))

        self.game_engine.add_stage(self)
        self.game_engine.set_active_stage(self)
