import pygame
import Engine
import Stage

pygame.init()

display_width = 800
display_height = 600
resolution = (display_width, display_height)

game_display = pygame.display.set_mode(resolution)
pygame.display.set_caption("Project Golf")
icon = pygame.image.load("media/start/test.png").convert()
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


def game_loop():

    game_engine = Engine.Engine()
    Stage.Stage.create_title_screen(game_engine)

    while True:
        game_engine.handle_input()
        game_engine.step()
        game_engine.draw(game_display)

        pygame.display.update()

        clock.tick(120)


game_loop()