import pygame, sys
from main import main

def home_screen():
    pygame.init()

    SCREEN_WIDTH = 700 
    SCREEN_HEIGHT = 700 
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        SCREEN.fill("white")
        FONT_SIZE = 20
        FONT_TYPE = 'freesansbold.ttf'
        FONT = pygame.font.Font(FONT_TYPE, FONT_SIZE)

        text_list = [
            ('Controls:', (350, 150), (0, 0, 0)),
            ('W, A, S, D to move', (350, 200), (0, 0, 0)),
            ('Left and right arrow keys to turn slowly. Space to shoot !', (350, 250), (0, 0, 0)),
            ('Press enter to start !', (350, 300), (0, 0, 0))
        ]

        for text in text_list:
            text_surface = FONT.render(text[0], True, text[2])
            text_rect = text_surface.get_rect(center=text[1])
            SCREEN.blit(text_surface, text_rect)

        key = pygame.key.get_pressed()
        if key[pygame.K_RETURN]:
            main()   

        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

pygame.quit()

if __name__ == '__main__':
    home_screen()
