import pygame
class Goal:   
    points = 0

    def __init__(self, goal, x, y):
        self.goal = goal
        self.x = x
        self.y = y
        goal_rect = self.goal.get_rect()
        new_width = int(goal_rect.width * 0.7)
        new_height = int(goal_rect.height * 0.7)

        # Create a new rectangle with the smaller size and centered in the original rectangle 
        small_goal_rect = pygame.Rect(0, 0, new_width, new_height)
        small_goal_rect.center = goal_rect.center

        # Update the position of the rectangle based on the position of the image
        small_goal_rect.x = self.x + goal_rect.width / 2 - small_goal_rect.width / 2
        small_goal_rect.y = self.y + goal_rect.height / 2 - small_goal_rect.height / 2

        self.goalRect = small_goal_rect