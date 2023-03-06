import pygame
import random

pygame.init()

screen_hieght = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width,screen_hieght))

pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    

    screen.fill((0,0,0))
    pygame.display.update()