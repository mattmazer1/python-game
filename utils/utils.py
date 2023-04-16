import pygame, random
from ball.ball import Ball
from goal.goal import Goal

def set_field(screen, screen_width, screen_height):
    NUM_COLS = 5
    NUM_ROWS = 5
    TILE_SIZE = screen_width

    # draw the horizontal lines
    for i in range(NUM_ROWS + 1):
        pygame.draw.rect(screen, (80, 81, 84), (0, i * TILE_SIZE / NUM_ROWS - 1, screen_width, 2))

    # draw the vertical lines
    for i in range(NUM_COLS + 1):
        pygame.draw.rect(screen, (80, 81, 84), (i * TILE_SIZE / NUM_COLS - 1, 0, 2, screen_height))

def gen_coords(start, end):
    return (random.randint(start, end), random.randint(start, end))

new_field_balls = []

def generate_balls(n):
    for i in range(n):
        coords = gen_coords(30, 650)
        ball = Ball(coords[0], coords[1])
        new_field_balls.append(ball)
    return new_field_balls

def reset():
    SCREEN_WIDTH = 700  
    SCREEN_HEIGHT = 700
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()

    LEFT_GOAL = pygame.image.load("./Assets/redGoal.svg")
    SCALED_LG = pygame.transform.scale(LEFT_GOAL, (80, 80))

    RIGHT_GOAL = pygame.image.load("./Assets/blueGoal.svg")
    SCALED_RG = pygame.transform.scale(RIGHT_GOAL, (80, 80))

    L_GOAL = Goal(SCALED_LG, 0, 0)
    R_GOAL = Goal(SCALED_RG, 620, 0)

    return (
        SCREEN_WIDTH,
        SCREEN_HEIGHT,
        SCREEN,
        clock,
        SCALED_LG,
        SCALED_RG,
        L_GOAL,
        R_GOAL,
    )

def gen_new_set():
    if len(new_field_balls) == 10:
        generate_balls(20)
