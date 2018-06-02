import pygame
import GameObject
import time


class SwingBar(GameObject.GameObject):

    def __init__(self):
        super().__init__(3)
        self.POWER_METER_IMG = pygame.image.load("media/game/pb_full.png").convert()
        self.POWER_METER_POS_X = int(self.DISPLAY_WIDTH / 4)
        self.POWER_METER_POS_Y = int(self.DISPLAY_HEIGHT * 0.95)

        self.POW_TICKER = pygame.image.load("media/game/tick.png").convert()
        self.pow_ticker_pos_x = self.POWER_METER_POS_X
        self.pow_ticker_pos_y = self.POWER_METER_POS_Y - 10
        self.pow_ticker_speed = 0

        self.ACC_TICKER = pygame.image.load("media/game/tick2.png").convert()
        self.acc_ticker_pos_x = 0
        self.acc_ticker_pos_y = self.pow_ticker_pos_y + 5
        self.acc_ticker_speed = 0

        self.power = 0
        self.power_num = 0
        self.accuracy = 0

        self.is_setting_power = False
        self.is_setting_accuracy = False

        self.accuracy_range = 50

        self.swing_sound = pygame.mixer.Sound("media/game/golf_swing.ogg")

    def draw(self, game_display):
        game_display.blit(self.POWER_METER_IMG, (self.POWER_METER_POS_X, self.POWER_METER_POS_Y))
        game_display.blit(self.POW_TICKER, (self.pow_ticker_pos_x, self.pow_ticker_pos_y))
        if self.acc_ticker_pos_x != 0:
            game_display.blit(self.ACC_TICKER, (self.acc_ticker_pos_x, self.acc_ticker_pos_y))

    def handle_input(self, stage, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.is_setting_power:
                        self.lock_power()
                        self.start_down_swing()
                    elif self.is_setting_accuracy:
                        self.lock_accuracy()
                        self.swing_sound.play()
                        time.sleep(0.5)
                        self.reset_swing_bar()
                    else:
                        self.start_up_swing()

    def step(self, stage):
        self.check_power_in_range()
        self.pow_ticker_pos_x += self.pow_ticker_speed

        self.check_accuracy_in_range()
        self.acc_ticker_pos_x += self.acc_ticker_speed

    def lock_power(self):
        self.is_setting_power = False
        self.pow_ticker_speed = 0

    def lock_accuracy(self):
        self.is_setting_accuracy = False
        self.power = int((self.pow_ticker_pos_x - self.POWER_METER_POS_X) / 3)
        self.power_num = self.power

        self.accuracy = 100 - int(abs(self.acc_ticker_pos_x - self.POWER_METER_POS_X))

    def start_up_swing(self): # Sets power
        self.is_setting_power = True
        self.pow_ticker_speed = 4

    def start_down_swing(self): # Sets accuracy
        self.is_setting_accuracy = True
        self.acc_ticker_pos_x = self.pow_ticker_pos_x
        self.acc_ticker_speed = -4

    def check_power_in_range(self):
        if self.pow_ticker_pos_x > 398 + self.POWER_METER_POS_X and self.is_setting_power:
            self.is_setting_power = False
            self.pow_ticker_speed = -8
        if self.pow_ticker_pos_x == self.POWER_METER_POS_X and self.pow_ticker_speed < 0:
            self.pow_ticker_speed = 0

    def check_accuracy_in_range(self):
        if self.acc_ticker_pos_x <= self.POWER_METER_POS_X - 50 and self.is_setting_accuracy:  # Occurs when space bar is not pressed 50 pixels after the start of the power bar
            self.is_setting_accuracy = False
            self.accuracy = 10
            time.sleep(0.5)
            self.acc_ticker_pos_x = 0
            self.pow_ticker_pos_x = self.POWER_METER_POS_X
            print("Accuracy: {}%".format(self.accuracy))

    def reset_swing_bar(self):
        self.pow_ticker_pos_x = self.POWER_METER_POS_X
        self.acc_ticker_pos_x = 0
        self.acc_ticker_speed = 0
