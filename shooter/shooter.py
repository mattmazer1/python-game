import pygame, math
class Shooter:
    SCREEN_WIDTH = 700  
    SCREEN_HEIGHT = 700
    BOT_WIDTH = 100
    BOT_HEIGHT = 100

    BOT = pygame.image.load("./Assets/robot.svg")
    SCALED_BOT = pygame.transform.scale(BOT, (BOT_WIDTH, BOT_HEIGHT))

    FIRST_BOT = pygame.image.load("./Assets/robot1.svg")
    FIRST_SCALED_BOT = pygame.transform.scale(FIRST_BOT, (BOT_WIDTH, BOT_HEIGHT))

    SECOND_BOT = pygame.image.load("./Assets/robot2.svg")
    SECOND_SCALED_BOT = pygame.transform.scale(SECOND_BOT, (BOT_WIDTH, BOT_HEIGHT))

    THIRD_BOT = pygame.image.load("./Assets/robot3.svg")
    THIRD_SCALED_BOT = pygame.transform.scale(THIRD_BOT, (BOT_WIDTH, BOT_HEIGHT))

    intake = 0
    MAX_INTAKE = 2
    COAST_RATE = 80
    space_pressed = False
    disable_shooter = False
    coast_u = False
    coast_d = False
    balls = []
    shoot_ball = []

    def __init__(self, angle, prec_angle_speed, angle_speed, speed, x, y):
        self.precision_angle_speed = prec_angle_speed
        self.angle = angle
        self.angle_speed = angle_speed
        self.speed = speed
        self.x = x
        self.y = y

    def is_valid_movement(self, move_x, move_y):
        if (
            self.x + move_x >= 50 
            and self.x + move_x <= self.SCREEN_WIDTH - 50
            and self.y + move_y >= 50
            and self.y + move_y <= self.SCREEN_HEIGHT - 50
        ):
            return True
        else:
            return False

    def coasting(self, move_x, move_y, num):
        self.x += move_x 
        self.y += move_y

        self.speed -= 20 / self.COAST_RATE

        if self.speed <= 0:
            self.speed = 0
            if num == 1:
                self.coast_u = False
            elif num == 2:
                self.coast_d = False

    def robot_movement(self, key):
        if not self.disable_shooter:
            moveU_x = self.speed * math.cos(math.radians(self.angle + 90))
            moveU_y = -self.speed * math.sin(math.radians(self.angle + 90))

            moveD_x = -self.speed * math.cos(math.radians(self.angle + 90))
            moveD_y = self.speed * math.sin(math.radians(self.angle + 90))

            if not self.coast_u:
                if key[pygame.K_w]:
                    self.speed = 5
                    if self.is_valid_movement(moveU_x, moveU_y):
                        self.x += moveU_x
                        self.y += moveU_y
            else:
                if self.is_valid_movement(moveU_x, moveU_y): 
                    if key[pygame.K_s]:
                        self.coast_u = False
                    else:
                        self.coasting(moveU_x, moveU_y, 1)

            if key[pygame.K_a]:
                self.angle += self.angle_speed

            if key[pygame.K_LEFT]:
                self.angle += self.precision_angle_speed

            if not self.coast_d:
                if key[pygame.K_s]:
                    self.speed = 5
                    if self.is_valid_movement(moveD_x, moveD_y):
                        self.x += moveD_x
                        self.y += moveD_y
            else:
                if self.is_valid_movement(moveD_x, moveD_y): 
                    if key[pygame.K_w]:
                        self.coast_d = False
                    else:
                        self.coasting(moveD_x, moveD_y, 2)
                        
            if key[pygame.K_d]:
                self.angle -= self.angle_speed

            if key[pygame.K_RIGHT]:
                self.angle -= self.precision_angle_speed

    def shooter_on_intake(self):
        if self.intake == 1:
            rotated_image = pygame.transform.rotate(self.FIRST_SCALED_BOT, self.angle)

        elif self.intake == 2:
            rotated_image = pygame.transform.rotate(self.SECOND_SCALED_BOT, self.angle)

        elif self.intake == 3:
            rotated_image = pygame.transform.rotate(self.THIRD_SCALED_BOT, self.angle)

        else:
            rotated_image = pygame.transform.rotate(self.SCALED_BOT, self.angle)

        return rotated_image
    
    def shooter_collider(self):
        c_rect = self.SCALED_BOT.get_rect(center = (self.x, self.y -40))
        c_rect = c_rect.inflate(-75, -75)

        pivot = pygame.math.Vector2(self.x, self.y)

        p0 = (pygame.math.Vector2(c_rect.topleft) - pivot).rotate(-self.angle) + pivot
        p1 = (pygame.math.Vector2(c_rect.topright) - pivot).rotate(-self.angle) + pivot 
        p2 = (pygame.math.Vector2(c_rect.bottomright) - pivot).rotate(-self.angle) + pivot 
        p3 = (pygame.math.Vector2(c_rect.bottomleft) - pivot).rotate(-self.angle) + pivot

        # Find the minimum and maximum x and y coordinates
        min_x = min(p0.x, p1.x, p2.x, p3.x)
        max_x = max(p0.x, p1.x, p2.x, p3.x)
        min_y = min(p0.y, p1.y, p2.y, p3.y)
        max_y = max(p0.y, p1.y, p2.y, p3.y)

        shooter_rect = pygame.Rect(min_x, min_y, max_x - min_x, max_y - min_y)

        return shooter_rect
    
    def pick_up(self, SCREEN, field_balls, shooter_rect):
        for ball in field_balls:
            if (
                ball is not None
                and ball.ball_rect is not None
                and self.intake >= 0
                and self.intake <= self.MAX_INTAKE
                and shooter_rect.colliderect(ball.ball_rect)
            ):
                self.intake += 1
                self.shoot_ball.append(False)
                field_balls.remove(ball)

            if ball is not None:
                SCREEN.blit(ball.SCALED_BALL, (ball.x, ball.y))

    def shoot_system(self, key):
        if not self.disable_shooter:
            if (self.intake > 0 and self.intake <= 3 and key[pygame.K_SPACE] and not self.space_pressed):
                self.intake -= 1  
                self.space_pressed = True
                for i in range(len(self.shoot_ball)):
                    if not self.shoot_ball[i]:
                        self.shoot_ball[i] = True
                        break
