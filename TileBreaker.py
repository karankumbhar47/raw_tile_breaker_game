import pygame
import random

pygame.init()

screen_hieght = 600
screen_width = 800

screen = pygame.display.set_mode((screen_width,screen_hieght))

pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)



# slider 
sliderImg = pygame.image.load('./images/53-Breakout-Tiles.png')
sliderX = 0
sliderY = 550
sliderX_change = 0

def slider(x,y):
    screen.blit(sliderImg,(x,y))



running = True

while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            print("while")
            if event.key == pygame.K_LEFT:
                sliderX_change = -0.6
            if event.key == pygame.K_RIGHT:
                sliderX_change = 0.6
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                sliderX_change = 0
                
    #slider
    sliderX += sliderX_change
    if sliderX <=0 :
        sliderX = 0
    elif sliderX >= 680:
        sliderX = 680

    slider(sliderX,sliderY)
            
    pygame.display.update()