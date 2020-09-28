import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 255, 255))
orange = (255, 106, 10)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 55)
syr = (225, 0, 255)
colorx = (180, 141, 141)
blue = (141, 202, 204)
def three(x, y):
    polygon(screen, syr, ([x, y], [x + 20, y - 22], [x + 40, y]))

circle(screen, orange, (400, 750), 300)
circle(screen, colorx, (400, 400), 250)
circle(screen, blue, (300, 350), 30)
circle(screen, blue, (500, 350), 30)
circle(screen, black, (300, 350), 10)
circle(screen, black, (500, 350), 10)
polygon(screen, red,[[300, 500], [500, 500], [400, 600]])
three(100, 100)
pygame.display.update()
clock = pygame.time.Clock()
finished = False



while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
