import pygame
import timer.timer
from utils.utils import generate_balls, new_field_balls

def finish_screen(SCREEN, L_GOAL, shooter, key):
    SCREEN.fill("white")

    FONT_SIZE = 30
    FONT_TYPE = "freesansbold.ttf"
    FONT = pygame.font.Font(FONT_TYPE, FONT_SIZE)

    text_list = [
        ("Game over!", (350, 200), (0, 0, 0)),
        ("You score was: " + str(L_GOAL.points), (350, 250), (0, 0, 0)),
        ("Press enter to start a new game !", (350, 300), (0, 0, 0)),
    ]

    for text in text_list:
        text_surface = FONT.render(text[0], True, text[2])
        text_rect = text_surface.get_rect(center=text[1])
        SCREEN.blit(text_surface, text_rect)

    for ball in new_field_balls:
        new_field_balls.remove(ball)

    for s_ball in shooter.shoot_ball:
        shooter.shoot_ball.remove(s_ball)
    
    if key[pygame.K_RETURN]: 
        timer.timer.time_val = 30
        timer.timer.stop_time = False
        generate_balls(20)
        shooter.intake = 0
        L_GOAL.points = 0
        shooter.x , shooter.y, shooter.angle = 100, 500, 0
        shooter.coast_u, shooter.coast_d = False, False
        shooter.disable_shooter = False