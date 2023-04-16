import pygame

def display_score(screen, goal):
    FONT_SIZE = 20
    FONT_TYPE = 'freesansbold.ttf'
    FONT = pygame.font.Font(FONT_TYPE, FONT_SIZE)

    text_surface_obj = FONT.render('Score:' + str(goal.points), True, (255, 255, 255))

    text_rect_obj = text_surface_obj.get_rect()

    text_rect_obj.center = (200, 20)

    screen.blit(text_surface_obj, text_rect_obj)


