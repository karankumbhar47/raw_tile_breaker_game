import pygame
import random

pygame.init()

screen_hieght = 800
screen_width = 836

screen = pygame.display.set_mode((screen_width,screen_hieght))

pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)



# slider 
sliderImg = pygame.image.load('./images/53-Breakout-Tiles.png')
sliderX = 0
sliderY = screen_hieght - 50
sliderX_change = 0

def slider(x,y):
    screen.blit(sliderImg,(x,y))



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
    screen.blit(tileImg, (x, y))


running = True
flag = 0
while running:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
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
    elif sliderX >= screen_width - 120 :
        sliderX = screen_width - 120

    slider(sliderX,sliderY)


    #TILES    
    for i in range(len(tilePositionArray)):
        tile(tilePositionArray[i][0],tilePositionArray[i][1],tilePositionArray[i][2],)
    
    
    pygame.display.update()