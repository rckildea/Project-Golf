import GameObject


class PlayerCharacter(GameObject.GameObject):
    def __init__(self):
        super().__init__(1)
        self.name = "USER_NAME"
        self.status_points = 50
        self.strength = 0
        self.control = 0
        self.stroke_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.current_stroke = 0

    def draw(self, game_display):
        pass

    def handle_input(self, stage, events):
        pass

    def step(self, stage):
        pass

    def set_ability_point(self):
        pass

    def increment_current_stroke(self):
        self.current_stroke += 1

    def check_stroke_limit(self):
        if self.current_stroke >= 12:
            return True
        return False

    def update_stroke_list(self, hole, strokes):
        self.stroke_list[hole] = strokes
        self.current_stroke = 0