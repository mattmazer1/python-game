import pygame, sys
from score.score import display_score
from screens.finishScreen import finish_screen
from shooter.shooter import Shooter
from shooter.firing import *
from utils.utils import *
import timer.timer

def main():
    # setup
    pygame.init()

    (
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SCREEN,
        clock,
        SCALED_LG,
        SCALED_RG,
        L_GOAL,
        R_GOAL,
    ) = reset()

    shooter = Shooter(0, 1, 5, 5, 100, 500)
    generate_balls(20)

# game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    shooter.space_pressed = False
                if event.key == pygame.K_w:
                    shooter.coast_u = True
                if event.key == pygame.K_s:
                    shooter.coast_d = True

        SCREEN.fill((113, 119, 120))
        
        set_field(SCREEN, SCREEN_WIDTH, SCREEN_HEIGHT)

        display_score(SCREEN, L_GOAL)

        timer.timer.timer(SCREEN, shooter)

        SCREEN.blit(SCALED_LG, (L_GOAL.x, L_GOAL.y))
        SCREEN.blit(SCALED_RG, (R_GOAL.x, R_GOAL.y))

        key = pygame.key.get_pressed()
        shooter.robot_movement(key)
        shooter.shoot_system(key)

        shooter_rect = shooter.shooter_collider()

        ball_to_shooter(shooter)

        launch(SCREEN, shooter)

        ball_collision(SCREEN_WIDTH, SCREEN_HEIGHT, L_GOAL, R_GOAL, shooter)

        shooter.pick_up(SCREEN, new_field_balls, shooter_rect)

        gen_new_set()

        rotated_image = shooter.shooter_on_intake()

        # render shooter
        SCREEN.blit(rotated_image,(shooter.x - int(rotated_image.get_width() / 2), shooter.y - int(rotated_image.get_height() / 2)))

        if shooter.disable_shooter:
            finish_screen(SCREEN, L_GOAL, shooter, key)

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()

if __name__ == "__main__":
    main()
