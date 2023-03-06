import pygame
import random
from ball import Ball
from screen import Screen
from slider import Slider

pygame.init()

screen_hieght = 800
screen_width = 836

#creating screen object
scr = Screen(screen_hieght,screen_width)
#creating slider object 
slider = Slider(0,screen_hieght-50,scr)
#creating ball object
ball = Ball(slider.x_cor+40,slider.y_cor-20,scr,slider)


# giving title and logo
pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)




# Tiles
mudTileImg = pygame.image.load('./images/19-Breakout-Tiles.png')
steelTileImg = pygame.image.load('./images/17-Breakout-Tiles.png')
unbreakableTileImg = pygame.image.load('./images/07-Breakout-Tiles.png')

tileWidth = 106
tileHeight = 28
startTileX = [100,153]
startTileY = 100
tileXpointsA = [startTileX[0]+(tileWidth*i) for i in range(0,6)]
tileXpointsB = [startTileX[1]+(tileWidth*i) for i in range(0,5)]
tileYpoints = [startTileY+(tileHeight*i) for i in range(0,11)]

tilePositionArray = []
for i in range(len(tileYpoints)):
    for j in range(len(tileXpointsA)):
        randomTile = random.choice([mudTileImg,steelTileImg,unbreakableTileImg])
        tilePositionArray.append([tileXpointsA[j],tileYpoints[i],randomTile])


def tile(x, y, tileImg):
    scr.screen.blit(tileImg, (x, y))


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
                slider.x_change = -0.6
            if event.key == pygame.K_RIGHT:
                slider.x_change = 0.6
            if event.key == pygame.K_SPACE:
                ball.state = "moving"  

        #key release upward
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
                
    
    slider.move()
    # #slider
    # sliderX += sliderX_change
    # if sliderX <=0 :
    #     sliderX = 0
    # elif sliderX >= screen_width - 120 :
    #     sliderX = screen_width - 120

    # slider(sliderX,sliderY)

    #ball
    # ball.move_ball(ball.x_cor.ball.y_cor)
    # ball.build(screen,sliderX+40,sliderY-20)
    if ball.state == "moving":
        ball.move_ball()
    else:
        ball = Ball(slider.x_cor+40,slider.y_cor-20,scr,slider)
    
    


    #TILES    
    for i in range(len(tilePositionArray)):
        tile(tilePositionArray[i][0],tilePositionArray[i][1],tilePositionArray[i][2],)
    

    pygame.display.update()