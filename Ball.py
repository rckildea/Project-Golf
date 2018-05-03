import pygame
import GameObject
import time
import math


class Ball(GameObject.GameObject):
    def __init__(self, x, y):
        super().__init__(2)
        self.ball_img = pygame.image.load("media/game/ball.png")
        self.ball_pos_x = int(x)
        self.ball_pos_y = int(y)
        self.ball_rect = self.ball_img.get_rect()
        self.update_rect()

        self.direction_arrow_img = pygame.image.load("media/game/direction_arrow.png")
        self.direction_angle = 0
        self.direction_angle_modifier = 0

        self.step_x = 0
        self.step_y = 0

        self.travel_distance_x = 0
        self.travel_distance_y = 0

    def draw(self, game_display):
        # Draw direction arrow
        self.update_arrow(game_display)

        # Draw ball
        game_display.blit(self.ball_img, (self.ball_pos_x, self.ball_pos_y))
        self.update_rect()

    def handle_input(self, stage, events):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.direction_angle_modifier = 2
        elif keys[pygame.K_RIGHT]:
            self.direction_angle_modifier = -2
        else:
            self.direction_angle_modifier = 0

    def step(self, stage):
        self.direction_angle += self.direction_angle_modifier

        self.get_power(stage)
        self.check_in_hole(stage)




    @staticmethod
    def rot_center(image, rect, angle):
        rot_image = pygame.transform.rotate(image, angle)
        rot_rect = rot_image.get_rect(center=rect.center)
        return rot_image, rot_rect

    def update_rect(self):
        self.ball_rect.x = self.ball_pos_x
        self.ball_rect.y = self.ball_pos_y

    def update_arrow(self, game_display):
        if self.travel_distance_x == 0:
            self.direction_arrow_img = pygame.image.load("media/game/direction_arrow.png")
            old_rect = self.direction_arrow_img.get_rect(center=(self.ball_rect.centerx, self.ball_rect.centery))
            self.direction_arrow_img, new_rect = Ball.rot_center(self.direction_arrow_img, old_rect, self.direction_angle)
            game_display.blit(self.direction_arrow_img, new_rect)

    def get_power(self, stage):
        step_count = 20  # Adjust to determine smoothness of golf ball travelling animation
        if stage.swing_bar.power != 0:
            # Calculate travel distances
            self.travel_distance_x = int(-(math.sin(math.radians(self.direction_angle)) * stage.swing_bar.power))
            self.travel_distance_y = int(-(math.cos(math.radians(self.direction_angle)) * stage.swing_bar.power))
            self.step_x = self.travel_distance_x / step_count
            self.step_y = self.travel_distance_y / step_count
            self.travel_distance_x = abs(self.travel_distance_x)
            self.travel_distance_y = abs(self.travel_distance_y)

        stage.swing_bar.power = 0

        if self.travel_distance_x > 0 or self.travel_distance_y > 0:
            self.ball_pos_x += self.step_x
            self.ball_pos_y += self.step_y

            self.travel_distance_x -= abs(self.step_x)
            self.travel_distance_y -= abs(self.step_y)

            time.sleep(0.015)
        else:
            self.travel_distance_x = 0
            self.travel_distance_y = 0

    def check_in_hole(self, stage):
        if (self.ball_rect.colliderect(stage.pin.pin_rect)):
            self.ball_pos_x = 0
            self.ball_pos_y = 0
            self.update_rect()
            print("Goal!")