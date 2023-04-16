import math
from ball.ball import Ball

def ball_to_shooter(shooter):
    for ball in shooter.shoot_ball:
        if ball:
            new_ball = Ball(shooter.x, shooter.y)
            new_ball.direction = (
                math.cos(math.radians(shooter.angle + 90)),
                -math.sin(math.radians(shooter.angle + 90)),
            )
            shooter.balls.append(new_ball)  
            shooter.shoot_ball.remove(ball)

def launch(SCREEN, shooter):
    for ball in shooter.balls:
        speed = 15  
        ball.x += speed * ball.direction[0]
        ball.y += speed * ball.direction[1]

        ball.ball_rect = ball.SCALED_BALL.get_rect(center=(ball.x, ball.y))
        
        position = (
            ball.x - int(ball.SCALED_BALL.get_width() / 2),
            ball.y - int(ball.SCALED_BALL.get_height() / 2),
        )
        SCREEN.blit(ball.SCALED_BALL, position)

def ball_collision(SCREEN_WIDTH, SCREEN_HEIGHT, L_GOAL, R_GOAL, shooter):
    for balls in shooter.balls:
        if L_GOAL.goalRect.colliderect(balls.ball_rect) or R_GOAL.goalRect.colliderect(
            balls.ball_rect
        ):
            L_GOAL.points += 1
            shooter.balls.remove(balls)

        elif balls.x < 0 or balls.x > SCREEN_WIDTH:
            shooter.balls.remove(balls)

        elif balls.y < 0 or balls.y > SCREEN_HEIGHT:
            shooter.balls.remove(balls)