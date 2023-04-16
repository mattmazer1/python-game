import pygame
class Ball:
    BALL = pygame.image.load("./Assets/ball.svg")
    SCALED_BALL = pygame.transform.scale(BALL, (15, 15))

    def __init__(self, x, y):
        self.x = x 
        self.y = y
        self.ball_rect = self.SCALED_BALL.get_rect(center=(self.x + 5, self.y + 5))
        self.direction = None

    
