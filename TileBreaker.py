import pygame
import random
from ball import Ball
from screen import Screen
from slider import Slider
from tile import Tile

pygame.init()

screen_hieght = 800
screen_width = 836

#creating screen object
scr = Screen(screen_hieght,screen_width)
#creating slider object 
slider = Slider(0,screen_hieght-50,scr)
#creating ball object
ball = Ball(slider.x_cor+53-16,slider.y_cor-32,scr,slider)
#creating tile object
tile = Tile(scr,ball)



# giving title and logo
pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)

running = True
while running:
    #filling color into screen
    scr.screen.fill((0,0,0))
    

    #key events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #key pressed downword
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                slider.x_change = -1.6
            if event.key == pygame.K_RIGHT:
                slider.x_change = 1.6
            if event.key == pygame.K_SPACE:
                ball.state = "moving"  

        #key release upward
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
                
    
    slider.move()
    ball.move_ball()
    tile.collition()
    tile.displayPattern()

    pygame.display.update()