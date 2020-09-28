import pygame, sys
from pygame.draw import *
pygame.init()
FPS = 30
screen = pygame.display.set_mode((400, 400))
screen.fill((255, 255, 255))
yel = (213, 227, 11)
red = (250, 7, 92)
black = (0, 0, 0)
circle(screen, yel, (200, 200), 100)
circle(screen, red, (170, 180), 20)
circle(screen, red, (230, 180), 20)
circle(screen, black, (230, 180), 10)
circle(screen, black, (170, 180), 10)
rect(screen, black, (150, 220, 100, 30))

line(screen, black, (185, 160), (50, 50), 20)
line(screen, black, (235, 160), (300, 50), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
