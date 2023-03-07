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
ball = Ball(slider.x_cor + slider.width/2 ,slider.y_cor ,scr,slider)
#creating tile object
tile = Tile(scr,ball)



# giving title and logo
pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)


tile_width = 106
tile_height = 28
margin = 0
def draw_grid():
	for c in range(30):
		#vertical lines
		pygame.draw.line(scr.screen, (255,255,255), (100 + (c * tile_width), 0), (c * tile_width +100, screen_hieght - margin))
		#horizontal lines
		pygame.draw.line(scr.screen, (255,255,255), (0, c * tile_height+ 100), (screen_width, c * tile_height +100))



running = True
while running:
    #filling color into screen
    scr.screen.fill((0,0,0))
    
    # draw_grid()

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
                ball.x_cor += ball.dx * (1/2)
                ball.y_cor += ball.dy  * (1/2)
                ball.build(ball.x_cor,ball.y_cor)
                ball.state = "moving"

        #key release upward
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
                
    
    slider.move()
    ball.move_ball()
    # tile.collition()
    tile.displayPattern()

    pygame.display.update()