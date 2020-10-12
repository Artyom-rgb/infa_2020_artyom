import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 30
screen = pygame.display.set_mode((1200, 900))
#colors
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
#score
score = 0
#draw ball
#создаёт координаты одного кружка
def create_ball():
    x = randint(100,700)
    y = randint(100,500)
    r = randint(30,50)
    color = COLORS[randint(0, 5)]
    v_x = randint(-5, 5)
    v_y = randint(-5, 5)
    return x, y, r, color, v_x, v_y
def drow_ball(ball): 
    x, y, r, color, v_x, v_y = ball
    circle(screen, color, (x, y), r)
def move_ball(ball):
    x, y, r, color = ball
    x += randint(-5, 5)
    y += randint(-5, 5)
    return x, y, r, color
balls = []
for i in range(20):
    balls.append(create_ball())
#return coor ball
def is_clicked(event, ball):
    mx, my = event.pos
    x, y, r, color = ball
    if((x - mx)**2 + (y - my)**2 <= r**2):
        return 1
    return 0
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if(is_clicked(event, ball)):
                    score += 1
                    print('a')
    for i, ball in enumerate(balls):
        balls[i] = move_ball(ball)
        drow_ball(ball)
    #new_ball()
    #if event.type == pygame.MOUSEBUTTONDOWN:
     #   click(event)
    
    pygame.display.update()
    screen.fill(BLACK)
print(score)
pygame.quit()
