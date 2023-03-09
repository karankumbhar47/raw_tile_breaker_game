import pygame
import random
import time
from ball import Ball
from screen import Screen
from slider import Slider
from tile import Tile
from button import Button

pygame.init()

clock = pygame.time.Clock()
fps = 60

#variable
main_menu = True
screen_height = 800
screen_width = 836
level = 1
levelMax = 10
score =0

#creating screen object
scr = Screen(screen_height,screen_width)

# #creating slider object 
# slider = Slider(0,screen_height-50,scr)
# #creating ball object
# ball = Ball(slider.x_cor + slider.width/2 ,slider.y_cor ,scr,slider)
# ball.ball = ball
# #creating tile object
# tile = Tile(scr,ball)


def reset(scr):
    screen_height = scr.height
    #creating slider object 
    slider = Slider(0,screen_height-50,scr)
    #creating ball object
    ball = Ball(slider.x_cor + slider.width/2 ,slider.y_cor ,scr,slider)
    ball.ball = ball
    #creating tile object
    tile = Tile(scr,ball)
    return slider,ball,tile


slider,ball,tile = reset(scr)


# loading button images
restartBtn = pygame.image.load('./images/restart_btn.png')
saveBtn = pygame.image.load('./images/save_btn.png')
startBtn = pygame.image.load('./images/start_btn.png')
startBtn = pygame.transform.scale(startBtn,(180,80))
exitBtn = pygame.image.load('./images/exit_btn.png')
exitBtn = pygame.transform.scale(exitBtn,(180,80))

#creating button images
restartBtn = Button(screen_width//2 - 100, screen_height//2 -20,restartBtn,scr)
startBtn = Button(screen_width//2 - 200, screen_height//2 -40,startBtn,scr)
exitBtn = Button(screen_width//2 + 50, screen_height//2 -40,exitBtn,scr)



# giving title and logo
pygame.display.set_caption("Tile Breakers")
game_icon = pygame.image.load('./images/brick-breaker.png')
pygame.display.set_icon(game_icon)
water = pygame.image.load('./images/27-Breakout-Tiles.png')
backgroundImg = pygame.image.load('./images/background.jpg')
backgroundImg = pygame.transform.scale(backgroundImg,(screen_width,screen_height))
font = pygame.font.Font('freesansbold.ttf', 32)
heartImg = pygame.image.load('./images/60-Breakout-Tiles.png')
lifeArray = [heartImg]*3

tile_width = 106
tile_height = 28
margin = 0
def draw_grid():
	for c in range(30):
		#vertical lines
		pygame.draw.line(scr.screen, (255,255,255), (100 + (c * tile_width), 0), (c * tile_width +100, screen_height - margin))
		#horizontal lines
		pygame.draw.line(scr.screen, (255,255,255), (0, c * tile_height+ 100), (screen_width, c * tile_height +100))



running = True
while running:
    # clock.tick(fps)

    #filling color into screen
    scr.screen.fill((0,0,0))

    scr.screen.blit(backgroundImg,(0,0))
    if main_menu:
        if startBtn.draw():
            main_menu = False
        if exitBtn.draw():
            running = False
    else:
        draw_grid()

        #key events
        
        slider.move()
        ball.move_ball()
        score = tile.collition(score)
        tile.displayPattern()

        if ball.gameOver:
            tile.positionArray = []
            if restartBtn.draw():
                score = 0
                slider,ball,tile = reset(scr)
                level = 1
                ball.game_over = 0
        
        if tile.num == 0:
            tile.positionArray =[]
            level +=1
            if level >= levelMax:
                level=1
            text = font.render("level "+str(level), True, (255,255,255),)
            for i in range(100000):
                scr.screen.blit(text,(screen_width//2-10,screen_height//2-20))
            life = ball.life
            slider,ball,tile = reset(scr)
            ball.life = life
                
        text = font.render("Score :" + str(score), True, (255,255,255))
        scr.screen.blit(text,(0,0))
        text = font.render("level "+str(level), True, (255,255,255),)
        scr.screen.blit(text,(screen_width -110,10))
    
        

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
                ball.x_cor += ball.dx * (1/5)
                ball.y_cor += ball.dy  * (1/5)
                ball.build(ball.x_cor,ball.y_cor)
                ball.state = "moving"
            if event.key == pygame.K_s:
                ball.speed = 2
            if event.key == pygame.K_p:
                if ball.speed > 0:
                    ball.speed =0
                else:
                    ball.speed = 0.5

        #key release upward
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                slider.x_change = 0
            if event.key == pygame.K_s :
                ball.speed = 0.5
        
    pygame.display.update()
pygame.quit()