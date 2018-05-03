class Engine(object):
    def __init__(self):
        self.stage_list = []
        self.active_stage = 0
        self.title_screen_index = -1
        self.course_select_screen_index = -1

    def draw(self, game_display):
        self.active_stage.draw(game_display)

    def handle_input(self):
        self.active_stage.handle_input()

    def step(self):
        self.active_stage.step()

    def add_stage(self, stage):
        self.stage_list.append(stage)

    def delete_stage(self, stage):
        self.stage_list.remove(stage)

    def set_active_stage(self, stage):
        self.active_stage = self.stage_list[self.get_stage_index(stage)]

    def get_stage_index(self, the_stage):
        for stage in self.stage_list:
            if stage == the_stage:
                return self.stage_list.index(stage)
        return -1

