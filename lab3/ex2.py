import pygame
import math as mt
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
def three(x, y, angle):
    polygon(screen, syr, [(x, y), (x - 40 * mt.cos(mt.pi/2 - angle), y - 40 * mt.sin(mt.pi/2 - angle)), (x + 80 * mt.sqrt(3)/2 * mt.cos(angle), y - 80 * mt.sqrt(3)/2), (x + 40 * mt.cos(mt.pi/2 - angle), y + 40 * mt.sin(mt.pi/2 - angle)), (x, y)])

circle(screen, orange, (400, 750), 300)
circle(screen, colorx, (400, 400), 250)
circle(screen, blue, (300, 350), 30)
circle(screen, blue, (500, 350), 30)
circle(screen, black, (300, 350), 10)
circle(screen, black, (500, 350), 10)
polygon(screen, red,[[300, 500], [500, 500], [400, 600]])
x0 = 100
a = mt.pi/2
y0 = mt.sqrt(400**2 - x0**2)
for i in range(6):
    three(x0, y0 - 80, a)
    three(800 - x0, y0 - 80, a)
    x0 += 40
    a += mt.pi/10
    y0 = mt.sqrt(400**2 - x0**2)
three(400, 400 - 250, mt.pi/2)
f = pygame.font.Font(None, 80)
text = f.render("PYTHON is not AMAZING!", 1, (0, 0, 0), (0, 180, 0))
screen.blit(text, (10, 50))
three(400, 400, mt.pi/2)
polygon(screen, orange, [(100, 600), (100 - 40, 600 - 40), (100 + 30, 600 - 80), (170, 600 - 40), (100 + 80, 600)])
polygon(screen, orange, [(100 + 600, 600), (100 - 40 + 600, 600 - 40), (100 + 30 + 600, 600 - 80), (170, 600 - 40 + 600), (100 + 80 + 600, 600)])
line(screen, colorx, (100, 600), (50, 50), 30)
line(screen, colorx, (700, 600), (650, 50), 30)
pygame.display.update()
clock = pygame.time.Clock()
finished = False



while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
