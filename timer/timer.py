import pygame

time_val = 30
last_time = 0
stop_time = False
reset = False

def timer(screen, shooter):
    global time_val, last_time, stop_time

    FONT_SIZE = 20
    FONT_TYPE = "freesansbold.ttf"
    FONT = pygame.font.Font(FONT_TYPE, FONT_SIZE)

    current_time = pygame.time.get_ticks()
    
    if current_time - last_time >= 1000 and stop_time == False:
        last_time = current_time
        time_val -= 1

    if time_val <= 0:
        time_val = 0
        stop_time = True
        text = FONT.render("Time: " + str(time_val + 0.0), True, (255, 255, 255))
        shooter.disable_shooter = True
    else:
        text = FONT.render("Time: " + str(time_val + 0.0), True, (255, 255, 255))

    text_rect = text.get_rect()
    text_rect.center = (500, 20)

    screen.blit(text, text_rect)
